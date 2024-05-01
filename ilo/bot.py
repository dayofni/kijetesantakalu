
import discord
import json

from os.path import exists

from discord import Message, Guild, RawReactionActionEvent

from ilo.awen import awen_a
from ilo.musi import mu_a
        
ON_MESSAGE = [mu_a]
ON_REACT   = [awen_a]

DEFAULT_CONFIG = {
    "REACT_IGNORE_DAYS":   7,
    "STOP_MESSAGE_AMOUNT": 2
}

class IloClient(discord.Bot):
    
    # ! Dunder methods
    
    def __enter__(self):
        
        self.CONFIG = {}
        
        # Load default configs
        
        if exists("saved_configs.json"):
            
            with open("saved_configs.json", "r") as f:
                self.CONFIG = {int(k):v for k, v in json.loads(f.read()).items()}
        
        else:
            self.CONFIG = {}
        
        return self
        
    def __exit__(self, *exc):
        
        with open("saved_configs.json", "w") as f:
            f.write(json.dumps(self.CONFIG, indent=4))
    
    # ! Guild methods
    
    def add_guild(self, guild: Guild):
        
        # if guild in saved data, load that
        
        # else
        
        self.CONFIG[guild.id] = DEFAULT_CONFIG.copy()
    
    async def on_ready(self):
        
        print(f'Logged on as {self.user}!')
        
        for guild in [i for i in self.guilds if i.id not in self.CONFIG]:
            self.add_guild(guild)
        
        print(self.CONFIG)
        
    async def on_guild_join(self, guild: Guild):
        
        print("Joined: ", guild)
        
        self.add_guild(guild)
    
    async def on_guild_remove(self, guild: Guild):
        
        print("Left:   ", guild)
        
        del self.CONFIG[guild.id]
    
    # ! Callbacks

    async def on_message(self, message: Message):
        
        if message.author == self.user:
            return
        
        print(f'Message from {message.author}: {message.content}')
        
        for func in ON_MESSAGE:
            await func(self, message, config=self.CONFIG[message.guild.id])
    
    async def on_raw_reaction_add(self, payload: RawReactionActionEvent):
        
        print(payload)
        
        user, reaction = payload.member, payload.emoji
        
        message = self.get_message(payload.message_id)
        
        if message.author == self.user:
            return
        
        if not message:
            print("Couldn't find attached message.")
            return
        
        print(f"Reaction from {user} on message {payload.message_id}: {reaction.name}")
        
        for func in ON_REACT:
            await func(self, user, reaction, message, config=self.CONFIG[payload.guild_id])