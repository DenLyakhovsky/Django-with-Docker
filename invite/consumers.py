import json

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Отримати ID користувача з URL-параметра
        self.user_id = self.scope['url_route']['kwargs']['user_id']

        # Приєднатися до кімнати з ID користувача
        await self.channel_layer.group_add(
            self.user_id,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Від'єднатися від кімнати з ID користувача
        await self.channel_layer.group_discard(
            self.user_id,
            self.channel_name
        )

    async def receive(self, text_data):
        # Обробка отриманих даних
        pass

    async def send_user_id(self):
        # Відправити ID користувача
        await self.send(text_data=str(self.user_id))
