import os
import random
import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Você logou como {bot.user}')



@bot.command()
async def meme(ctx):
    memes = random.choice(os.listdir('images'))
    with open(f'images/{memes}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("token")
