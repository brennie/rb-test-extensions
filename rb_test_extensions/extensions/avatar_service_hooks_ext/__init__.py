from djblets.avatars.services.base import AvatarService
from reviewboard.extensions.base import Extension
from reviewboard.extensions.hooks import AvatarServiceHook


class AwwvatarService(AvatarService):

    avatar_service_id = 'aww'
    name = 'Awwvatar Service'

    def get_avatar_urls_uncached(self, user, size):
        ext = AvatarServiceHooksExtension.instance
        return {
            '1x': ext.get_static_url('img/avatar256.png'),
            '2x': ext.get_static_url('img/avatar512.png'),
        }


class AvatarServiceHooksExtension(Extension):
    metadata = {
        'Name': 'Avatar Service Hooks Test Extension',
    }

    def initialize(self):
        AvatarServiceHook(self, AwwvatarService)
