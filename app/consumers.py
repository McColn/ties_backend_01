import json
from channels.generic.websocket import WebsocketConsumer
from .models import *

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        sender = text_data_json['sender']
        receiver = text_data_json['receiver']
        message = text_data_json['message']

        # Save message to the database
        Message.objects.create(sender=sender, receiver=receiver, text=message)

        # Broadcast message to the sender and receiver
        self.send(text_data=json.dumps({
            'sender': sender,
            'receiver': receiver,
            'message': message
        }))
