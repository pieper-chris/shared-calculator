from channels.generic.websocket import AsyncWebsocketConsumer, AsyncJsonWebsocketConsumer, JsonWebsocketConsumer
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.shortcuts import HttpResponse
import asyncio
import json


class UConsumer(JsonWebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)('index', self.channel_name)
        self.accept()
        
    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)('index', self.channel_name)
        self.close()
        print(f'removed {self.channel_name}')

    def receive_json(self, content, **kwargs):
        # print("Received event: {}".format(content))
        async_to_sync(self.channel_layer.group_send)('index',
        {
            "type": "group.message",
            "content": content
        })
    
    # group.message handler
    def group_message(self, message):
        layer = get_channel_layer()
        self.send_json(
            {
            'type': 'index.send',
            'text': message
            }
        )
