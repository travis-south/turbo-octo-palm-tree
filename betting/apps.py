from django.apps import AppConfig


class BettingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'betting'

    def ready(self) -> None:
        import betting.signals
        return super().ready()
