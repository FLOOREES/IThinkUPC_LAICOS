import json

from members import models

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from .models import Room


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        # connection has to be accepted
        async_to_sync(self.channel_layer.group_add)("chat", self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)("chat", self.channel_name)
        pass

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print("receivedd")
        async_to_sync(self.channel_layer.group_send)(
            'chat',{
                'type': 'chat.message',
                'message': message,
                #'username': self.user
            }
        )

    def chat_message(self, event):
        message = event['message']
        #username = event['username']
        print("sent")
        #print(username)

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message,
            #'username': username
        }))