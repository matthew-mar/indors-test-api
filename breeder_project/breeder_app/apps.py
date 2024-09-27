from django.apps import AppConfig


class BreederAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'breeder_app'

    def ready(self) -> None:
        from .container import Container
        Container().wire(modules=[
            "breeder_app.serializers",
        ])
