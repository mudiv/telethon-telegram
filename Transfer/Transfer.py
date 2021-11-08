from telethon.sync import TelegramClient
from telethon import functions, types


client=TelegramClient('ruks', "7626141", "7d17edb761c2ac75b8e186555c69d1ad")

result = client(functions.channels.UpdateUsernameRequest(channel="يوزر قناة",username="يوزر"))

print(result)