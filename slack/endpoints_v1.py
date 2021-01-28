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
    'channels_info': {
        'path': '/channels.info',
        'valid_params': ['channel']
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
        'valid_params': ['channel','text','username','as_user','parse','link_names','attachments','unfurl_links','unfurl_media','username','as_user','icon_url','icon_emoji','thread_ts','reply_broadcast']
    },
    'chat_delete': {
        'path': '/chat.delete',
        'valid_params': ['channel','ts']
    },

    'conversations_history': {
        'path': '/conversations.history',
        'valid_params': ['channel','latest','oldest','inclusive','limit']
    },
    'conversations_info': {
        'path': '/conversations.info',
        'valid_params': ['channel','include_locale','include_num_members']
    },
    'conversations_list': {
        'path': '/conversations.list'
        'valid_params': ['exclude_archived','types']
    },
    'convesations_open': {
        'path': '/conversations.open',
        'valid_params': ['channel','return_im','users']
    },
    'conversations_set_topic': {
        'path': '/conversations.setTopic',
        'valid_params': ['channel','topic']
    },

    'files_delete': {
        'path': '/files.delete',
        'valid_params': ['file']
    },
    'files_info': {
        'path': '/files.info',
        'valid_params': ['file','count','page']
    },
    'files_list': {
        'path': '/files.list',
        'valid_params': ['user','channel','ts_from','ts_to','types','count','page']
    },
    'files_revoke_public_url': {
        'path': '/files.revokePublicURL',
        'valid_params': ['file']
    },
    'files_shared_public_url': {
        'path': '/files.sharedPublicURL',
        'valid_params': ['file']
    },
    'files_revoke_public_url': {
        'path': '/files.revokePublicURL',
        'valid_params': ['file']
    },
    'files_upload': {
        'path': '/files.upload',
        'valid_params': ['file','content','filetype','filename','title','initial_comment','channels']
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

    'mpim_list': {
        'path': '/mpim.list'
    },
    'mpim_open': {
        'path': '/mpim.open',
        'valid_params': ['users']
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
