import discord
from discord.ext import commands
import sys,os
# import util from parent directory
sys.path.insert(0, os.path.abspath('..'))
from utils import *
TOKEN = get_token(get_directory() + "/token.txt")


class MyBot(commands.Bot):
    def __init__(self, command_prefix):
        super().__init__(command_prefix)
        
    async def on_ready(self):
        print(f"Bot connected as {self.user}")
    
    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello, I'm your Discord bot!")
        
    @commands.command()
    async def square(self, ctx, num: int):
        square = num ** 2
        await ctx.send(f"The square of {num} is {square}.")
        
    @commands.command()
    async def say(self, ctx, *, message):
        await ctx.send(message)
        
    @commands.command()
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount + 1)
    
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Invalid command. Please try again.")
    
    def run_bot(self):
        self.run(TOKEN)

bot = MyBot(command_prefix="!")
bot.run_bot()