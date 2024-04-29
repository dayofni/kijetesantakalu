
from discord import Message, Client

async def mu_a(client: Client, message: Message, config: dict = {}):
    
    if message.author == client.user:
        return
        
    if any(["".join(list(sorted(set(i.strip("`~!@#$%^&*()_-+={[}]|\\:;\"'<,>.?/"))))) == "mu" for i in message.content.lower().split()]):        
        await message.channel.send('mu a!')