from telethon.sync import TelegramClient
from telethon import functions, types


client=TelegramClient('ruks', api_id,api_hash)

result = client(functions.channels.UpdateUsernameRequest(channel="يوزر قناة",username="يوزر"))

print(result)

;