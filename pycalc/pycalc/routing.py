from channels.routing import ProtocolTypeRouter, URLRouter
# from my_proj.game.routing import websockets
'''from calculator.routing import websockets

from django.conf.urls import url
from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
from calculator.consumers import ws_connect, ws_disconnect'''


# from channels.routing import ProtocolTypeRouter
from calculator import consumers
from django.urls import path
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

# from channels.routing import route
from calculator.consumers import UConsumer

websocket_URLPattern=[
    path("",consumers.UConsumer),
]

application = ProtocolTypeRouter({
    #"websocket": websockets,
    "websocket":AllowedHostsOriginValidator(AuthMiddlewareStack(URLRouter(websocket_URLPattern))),
})
