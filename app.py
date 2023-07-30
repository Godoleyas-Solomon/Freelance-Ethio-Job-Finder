from telethon.sync import TelegramClient, events
import poe
import re
from config import *



poe_client = poe.Client(cookie)
client = TelegramClient('session', api_id, api_hash)
print('Started')

async def main():
    # print('Going on')
    @client.on(events.NewMessage(chats=channel))
    async def handler(event):
        # get the message text
        message = event.message.message
        job_title_pattern = r"Job Title:\s*(.*)"
        matched = re.search(job_title_pattern, message)
        if matched:
            job_title = matched.group(1)
            print(job_title)
        else:
            print("Job title not found")
        for chunk in poe_client.send_message(AI, f'{prompt}\n\n{job_title}'):
            pass
        reply = chunk['text']
        if int(reply) == True:
            print(True)
            await client.forward_messages(dump, event.message)
            poe_client.send_chat_break(AI)
        else:
            print(False)
            poe_client.send_chat_break(AI)


client.start()
client.loop.run_until_complete(main())
client.run_until_disconnected()
