from django.apps import AppConfig

#aplicacion actual y funcion para el bot de whatsapp

class WebConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'web'

    def ready(self):
        import web.signals
