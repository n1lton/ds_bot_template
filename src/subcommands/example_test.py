import discord
from discord.ext import commands


@commands.slash_command(name='test', description='test')
async def test(ctx: discord.ApplicationContext):
    await ctx.respond(ctx.author.display_name)


def setup(group: discord.SlashCommandGroup):
    test.parent = group
    group.add_command(test)