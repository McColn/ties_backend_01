from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from app.consumers import SMSConsumer

application = ProtocolTypeRouter({
    'websocket': URLRouter([
        path('ws/sms/', SMSConsumer.as_asgi()),
    ]),
})
