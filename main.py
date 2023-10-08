import os
import random
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)





@bot.command()
meml = 1
mem2 = 2
mem3 = 3
mem4 = 4
mem5 = 5
mem6 = 6
mem7 = 7

baza_mem = random.randint(1,5)
with open(f'images/{baza_mem.jpg}', 'rb') as f:
    picture = discord.File(f)
special_mem = random.randint(6,7)
with open(f'images/{special_mem}', 'rb') as f:
    picture = discord.File(f)

bot.run("MTE1Mjk2MDkxMzc3MTYwMjAwMQ.GcINRb.kSNEQDpcDu9g5Q-5DgjPO_nqLzfV5lNwlEOqM0")





