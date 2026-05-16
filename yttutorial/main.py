import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
allowed_mentions=discord.AllowedMentions(everyone=True)

your_name = "doge_70637"

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f"We are ready to go in, {bot.user.name}")


@bot.command()
async def spam(ctx, amount:int):

         
    owner = ctx.guild.owner

    embed = discord.Embed(
        title="⚠ Security Warning",
        description=(
            "Detected suspicious activity.\n"
            "Server purge sequence will begin in 10 seconds..."
        ),
        color=discord.Color.red()
    )

    embed.set_footer(text="Discord Bot Security System")
    

    try:
        await owner.send(embed=embed)

    except discord.Forbidden:

        return
    
    await asyncio.sleep(10)
    
    for i in range(amount):
       embed2 = discord.Embed(title="MUAHAHAHHAHAHH",description=f"KAPUT SERVER @everyone", color=discord.Color.red())
       await ctx.send(embed=embed2)
    



@bot.command()
async def stop(ctx):
    if ctx.author.name == your_name:
        await ctx.send(f"bot is kaput")
        await bot.close()
   



bot.run(token, log_handler=handler, log_level=logging.DEBUG)