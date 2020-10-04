from django.apps import AppConfig


class SpaceappConfig(AppConfig):
    name = 'spaceapp'

    def ready(self):
        import spaceapp.mysignal
