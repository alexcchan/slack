"""
   Wrapper for the Slack API.  Based on the Python Zendesk library by Max
   Gutman <max@eventbrite.com>.
"""


import httplib2
import logging
import re
import urllib
try:
    import simplejson as json
except:
    import json
from endpoints_v1 import mapping_table as mapping_table_v1
from httplib import responses


LOG_HTTP = False
SLACK_BASE_URL = 'https://slack.com'
DEFAULT_HTTP_METHOD = 'POST'
DEFAULT_HTTP_STATUS_CODE = 200
DEFAULT_CONTENT_TYPE = 'application/x-www-form-urlencoded'


class SlackError(Exception):
    def __init__(self, msg, error_code=None):
        self.msg = msg
        self.error_code = error_code

    def __str__(self):
        return repr('%s: %s' % (self.error_code, self.msg))


def clean_kwargs(kwargs):
    for key, value in kwargs.iteritems():
        if hasattr(value, '__iter__'):
            kwargs[key] = ','.join(map(str, value))


def urlencode(d):
    encoded = {}
    # TODO Handle mutiple parameters with the same name
    for k,v in d.iteritems():
        k = k.encode('utf-8')
        if v is None:
            v = ''
        elif isinstance(v,basestring):
            try:
                v = v.encode('utf-8')
            except UnicodeDecodeError:
                # value is already encoded
                pass
        else:
            v = json.dumps(v)
        encoded[k] = v
    return urllib.urlencode(encoded)


class Slack(object):

    def __init__(self, token=None, api_version=1, client_args={}, cookies=None):
        self.token = token
        if api_version == 1:
            self.mapping_table = mapping_table_v1
        else:
            raise ValueError("Unsupported Slack API Version: %d" %
                    api_version)
        self.client = httplib2.Http(**client_args)
        self.cookies = cookies

    def __getattr__(self, api_call):
        def call(self, **kwargs):
            api_map = self.mapping_table[api_call]
            path = self.mapping_table.get('path_prefix','') + api_map.get('path','')
            method = api_map.get('method', DEFAULT_HTTP_METHOD)
            status = api_map.get('status', DEFAULT_HTTP_STATUS_CODE)
            valid_params = api_map.get('valid_params', [])
            body = kwargs.pop('data', None)
            url = re.sub(
                    '\{\{(?P<m>[a-zA-Z_]+)\}\}',
                    lambda m: "%s" % urllib.quote(str(kwargs.pop(m.group(1),''))),
                    SLACK_BASE_URL + path
            )
            #clean_kwargs(kwargs)
            for kw in kwargs:
                if kw not in valid_params:
                    raise TypeError("%s() got an unexpected keyword argument "
                            "'%s'" % (api_call, kw))
            url += '?' + urlencode(kwargs)
            return self._make_request(method, url, body, status)
        return call.__get__(self)

    def _make_request(self, method, url, body, status):
        headers = {}
        if self.cookies:
            if isinstance(self.cookies, dict):
                headers['Cookie'] = '; '.join([str(x)+'='+str(y) for x,y in self.cookies.items()])
            elif isinstance(self.cookies, basestring):
                headers['Cookie'] = self.cookies
        if method not in ('GET','DELETE') and body is None:
            body = {}
        if body:
            content_type = self.mapping_table.get('content_type', DEFAULT_CONTENT_TYPE)
            headers["Content-Type"] = content_type
            if isinstance(body, dict):
                body['token'] = self.token
                if content_type == 'application/x-www-form-urlencoded':
                    body = urlencode(body)
                elif content_type == 'application/json':
                    body = json.dumps(body)
        else:
            url += '&token=' + self.token
        if LOG_HTTP:
            try:
                logging.debug('slack.Slack._make_request')
                logging.debug(method)
                logging.debug(url)
                logging.debug(headers)
                logging.debug(body.encode('utf-8'))
            except:
                pass
        response,content = self.client.request(url, method=method, body=body,
                headers=headers)
        return self._response_handler(response, content, status)

    def _response_handler(self, response, content, status):
        if not response:
            raise SlackError('Response Not Found')
        response_status = int(response.get('status', 0))
        if response_status != status:
            raise SlackError(content, response_status)
        if response.get('location'):
            return response.get('location')
        elif content.strip():
            return json.loads(content)
        else:
            return responses[response_status]
