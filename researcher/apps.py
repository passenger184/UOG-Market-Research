from django.apps import AppConfig


class ResearcherConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'researcher'

    def ready(self):
        import researcher.signals
