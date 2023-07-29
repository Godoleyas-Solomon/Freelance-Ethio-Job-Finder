from telethon.sync import TelegramClient, events
import poe
from config import *
import json


poe_client = poe.Client(cookie)

while True:
    message = input('> ')
    if message.lower() == 'quit':
        break
    else:
        for chunk in poe_client.send_message(AI, f'{prompt}\n\n{message}'):
            pass
        reply = chunk['text']
        if int(reply) == True:
            print(message)
            poe_client.send_chat_break(AI)
        else:
            print(False)
            poe_client.send_chat_break(AI)
