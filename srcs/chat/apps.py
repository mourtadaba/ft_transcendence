from django.apps import AppConfig


from django.apps import AppConfig

class ChatConfig(AppConfig):
    name = 'chat'
    def ready(self):
        import chat.signals