from django.apps import AppConfig


class GolfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'golf'

    def ready(self) -> None:
        from . import signals
