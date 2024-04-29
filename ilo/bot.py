
import discord

class ilo(discord.Client):
    
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        
        print(f'Message from {message.author}: {message.content}')
        
        if message.author == self.user:
            return
        
        if any(["".join(list(sorted(set(i.strip("`~!@#$%^&*()_-+={[}]|\\:;\"'<,>.?/"))))) == "mu" for i in message.content.lower().split()]):
            
            await message.channel.send('mu a!')