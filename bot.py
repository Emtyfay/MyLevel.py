from discord.ext import commands


import discord

import config


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot started!!")
    await bot.change_presence(status=discord.Status.online,
                              activity=discord.Game('MyLevel.py'))


@bot.command(aliases=['пинг'])
async def pong(ctx):
    await ctx.reply('pong')


bot.run(config.TOKEN)