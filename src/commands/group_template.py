import discord, os
from discord.ext import commands
from bot import bot

example = discord.SlashCommandGroup(
    name='example'
)

for filename in os.listdir('subcommands'):
    if filename.endswith('.py') and filename.startswith('example_'):
        module = __import__(f'subcommands.{filename.removesuffix(".py")}', fromlist=['setup'])
        module.setup(example)

def setup(bot: commands.Bot):
    bot.add_application_command(example)