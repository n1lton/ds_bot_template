import discord
from discord.ext import commands


@commands.slash_command(name='test', description='test')
async def test(ctx: discord.ApplicationContext):
    await ctx.respond(ctx.author.display_name)


def setup(bot: commands.Bot):
    bot.add_application_command(test)