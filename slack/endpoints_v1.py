"""
API MAPPING FOR Slack API V1
"""

mapping_table = {

    'content_type': 'application/x-www-form-urlencoded',
    'path_prefix': '/api',

    'api_test': {
        'path': '/api.test',
        'valid_params': ['format', 'auth_token']
    },

    'channels_history': {
        'path': '/channels.history',
        'valid_params': ['channel','latest','oldest','inclusive','count']
    },
    'channels_list': {
        'path': '/channels.list',
        'valid_params': ['exclude_archived']
    },

    'chat_post_message': {
        'path': '/chat.postMessage',
        'valid_params': ['channel', 'text','username','as_user','parse','link_names','attachments','unfurl_links','unfurl_media','icon_url','icon_emoji']
    },
    'chat_delete': {
        'path': '/chat.delete',
        'valid_params': ['channel','ts']
    },

    'im_list': {
        'path': '/im.list'
    },
    'im_open': {
        'path': '/im.open',
        'valid_params': ['user']
    },

    'pins_add': {
        'path': '/pins.add',
        'valid_params': ['channel','file','file_comment','timestamp']
    },
    'pins_list': {
        'path': '/pins.list',
        'valid_params': ['channel']
    },
    'pins_remove': {
        'path': '/pins.remove',
        'valid_params': ['channel','file','file_comment','timestamp']
    },

    'users_list': {
        'path': '/users.list'
    },

}
