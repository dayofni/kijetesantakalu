
import discord

from discord import Message, RawReactionActionEvent

from ilo.awen import awen_a
from ilo.musi import mu_a
        
ON_MESSAGE = [mu_a]
ON_REACT   = [awen_a]

CONFIG = {
    
    "REACT_IGNORE_DAYS":   7,
    "STOP_MESSAGE_AMOUNT": 5
}

class ilo(discord.Client):
    
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message: Message):
        
        print(f'Message from {message.author}: {message.content}')
        
        for func in ON_MESSAGE:
            await func(self, message, config=CONFIG)
    
    async def on_raw_reaction_add(self, payload: RawReactionActionEvent):
        
        user, reaction = payload.member, payload.emoji
        
        message = self.get_message(payload.message_id)
        
        if not message:
            print("Couldn't find attached message.")
            return
        
        for func in ON_REACT:
            await func(self, user, reaction, message, config=CONFIG)