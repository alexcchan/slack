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
    'channels_set_topic': {
        'path': '/channels.setTopic',
        'valid_params': ['channel','topic']
    },

    'groups_history': {
        'path': '/groups.history',
        'valid_params': ['channel','latest','oldest','inclusive','count']
    },
    'groups_list': {
        'path': '/groups.list',
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

    'emoji_list': {
        'path': '/emoji.list'
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

    'reactions_add': {
        'path': '/reactions.add',
        'valid_params': ['name','file','file_comment','channel','timestamp']
    },
    'reactions_get': {
        'path': '/reactions.get',
        'valid_params': ['file','file_comment','channel','timestamp','full']
    },
    'reactions_list': {
        'path': '/reactions.list',
        'valid_params': ['user','full','count','page']
    },
    'reactions_remove': {
        'path': '/reactions.remove',
        'valid_params': ['name','file','file_comment','channel','timestamp']
    },

    'search_messages': {
        'path': '/search.messages',
        'valid_params': ['query','sort','sort_dir','highlight','count','page']
    },

    'users_list': {
        'path': '/users.list',
        'valid_params': ['presence']
    },

}
