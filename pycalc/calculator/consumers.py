import json
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer, AsyncJsonWebsocketConsumer, JsonWebsocketConsumer
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.shortcuts import HttpResponse


#from channels import Group



# class UConsumer(AsyncWebsocketConsumer):
# class UConsumer(AsyncConsumer):
# class UConsumer(AsyncJsonWebsocketConsumer):
class UConsumer(JsonWebsocketConsumer):
    # async def connect(self):
    def connect(self):
        # await self.accept()
        # await self.channel_layer.group_add('index', self.channel_name)
        async_to_sync(self.channel_layer.group_add)('index', self.channel_name)
        self.accept()
        '''await self.channel_layer.send('index',
        {
            "type": "websocket.send",
            "text": "Hello World"
        })'''

    # async def disconnect(self, code):
    def disconnect(self, code):
        # print('disconnected')
        # await self.channel_layer.group_discard('index', self.channel_name)
        async_to_sync(self.channel_layer.group_discard)('index', self.channel_name)
        self.close()
        print(f'removed {self.channel_name}')


    def receive_json(self, content, **kwargs):
        print("Received event: {}".format(content))
        
        # self.send_json(content)
        async_to_sync(self.channel_layer.group_send)('index',
        {
            "type": "group.message",
            "content": "hi"
        })
        
    # async def websocket_receive(self, message):
    '''def websocket_receive(self, message):
        print("asdf", message)
        return super().websocket_receive(message)'''
        
    def group_message(self, message):
        layer = get_channel_layer()
        '''async_to_sync(layer.group_send)('index',
        {
            #"type": "websocket.send",
            'type': 'websocket.send',
            'content': 'message'
        })'''
        
        #return HttpResponse('<p>Done</p>')
        self.send_json(
            {
            'type': 'index.send',
            #'text': event['text']
            'text': message
            }
        )

    # async def websocket_ingest(self, event):
    '''def websocket_ingest(self, event):
        await self.send_json(event)'''
    '''async def websocket_connect(self, event):
        print("connected", event)
        await self.send({
            "type": "websocket.accept"
        })
        #await asyncio.sleep(5)
        await self.send({
            "type": "websocket.send",
            "text": "Hello World"
        })
        
    async def websocket_receive(self, event):
           # Broadcast
           print("receive", event)
           dat = event["text"]
           await self.send({
               "type": "websocket.send",
               "text": dat
           })

    async def websocket_disconnect(self, event):
            print("disconnect", event)'''
        
    
    
    
'''def ws_connect(message):
    Group('users').add(message.reply_channel)
    
def ws_disconnect(message):
    Group('users').discard(message.reply_channel)'''
