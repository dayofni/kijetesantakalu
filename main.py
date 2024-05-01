
import discord

from ilo.bot import IloClient, DEFAULT_CONFIG
from tomllib import loads

def main():
   
    with open("secrets.toml") as f:
        secrets = loads(f.read())

    intents = discord.Intents.all()

    with IloClient(intents=intents) as bot:

        #! Slash commands
        
        @bot.command(description="Edit server configs.")
        async def config(ctx: discord.ApplicationContext, 
                         param: discord.Option(str, "Select an item", choices=list(DEFAULT_CONFIG.keys())), # type: ignore
                         value: int):
            
            guild = ctx.guild_id
            
            print(bot.CONFIG)
            
            bot.CONFIG[guild][param] = value
            
            await ctx.respond(f"Set parameter {param} to {value}.")

        bot.run(secrets["token"])


if __name__ == "__main__":
    main()