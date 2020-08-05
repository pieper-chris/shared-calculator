#from channels.routing import route
#from calculator.consumers import ws_connect, we_disconnect

'''channel_routing = [
    route('websocket.connect', ws_connect),
    route('websocket.disconnect', ws_disconnect),
]'''

'''websockets = [
    route('websocket.connect', ws_connect),
    route('websocket.disconnect', ws_disconnect),
]
'''
'''from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from .consumers import LiveScoreConsumer
websockets = URLRouter([
    path('', views.home, name='home'),
])'''
