from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from calculator.consumers import UConsumer
from calculator import consumers
from django.urls import path

websocket_URLPattern=[
    path("",consumers.UConsumer),
]

application = ProtocolTypeRouter({
    "websocket":AllowedHostsOriginValidator(AuthMiddlewareStack(URLRouter(websocket_URLPattern))),
})
