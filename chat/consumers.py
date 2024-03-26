# chat/consumers.py

from channels.generic.websocket import WebsocketConsumer
import json

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Handle the received message (e.g., save to database, send to other clients)
        # Example: Echo the message back to the client
        self.send(text_data=json.dumps({
            'message': message
        }))
