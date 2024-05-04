
from discord import Message, Client

async def mu_a(client: Client, message: Message, config: dict = {}):
        
    if any(["".join(sorted(set(i.strip("`~!@#$%^&*()_-+={[}]|\\:;\"'<,>.?/")))) == "mu" for i in message.content.lower().split()]):        
        await message.channel.send('mu a!')