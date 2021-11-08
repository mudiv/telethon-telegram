from telethon.sync import TelegramClient
from telethon import functions, types


client=TelegramClient('ruks', api_id,api_hash)

result = client(functions.account.CheckUsernameRequest(username="->>user<<-"))

print(result)

