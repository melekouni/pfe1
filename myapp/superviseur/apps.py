
from django.apps import AppConfig


class MapConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = "superviseur"

    def ready(self):
        from . import mqtt
        mqtt.client.loop_start()    
