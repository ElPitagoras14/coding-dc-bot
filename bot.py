import discord
from discord.ext import commands
import datetime
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("TOKEN")

prefix = "c!"
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=prefix, description="this is a testing bot", help_command=None, intents=intents)


# Ping-pong
@bot.command()
async def ping(ctx):
    await ctx.send("pong")


# Help
@bot.command()
async def help(ctx):
    des = """
  WIP
  Comandos de Coding
  > ping: El bot te responde pong
  """
    embed = discord.Embed(
        title="I'm Coding",
        url="https://cdn.discordapp.com/app-icons/1010000544888279130/4590067d4dbe00de00007744f62adec7.png?size=1024",
        description=des,
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.blue(),
    )
    embed.set_footer(text="solicitado por: %s" % (ctx.author.name))
    embed.set_author(
        name="Coding",
        icon_url="https://cdn.discordapp.com/app-icons/1010000544888279130/4590067d4dbe00de00007744f62adec7.png?size=1024",
    )

    await ctx.send(embed=embed)

# Cambiar estado
@bot.event
async def on_ready():
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=("%shelp" % prefix)
        )
    )
    print("My bot is ready")

bot.run(token)
