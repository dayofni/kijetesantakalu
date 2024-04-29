
import discord

from ilo.bot import ilo
from tomllib import loads
        
def main():
    
    with open("secrets.toml") as f:
        secrets = loads(f.read())

    intents = discord.Intents.all()
    client = ilo(intents=intents)

    client.run(secrets["token"])

if __name__ == "__main__":
    main()