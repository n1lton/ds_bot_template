import discord
from discord.ext import commands

async def on_application_command_error(ctx: discord.ApplicationContext, error: Exception):
    if any(isinstance(error, exception) for exception in [commands.MissingRole, commands.MissingAnyRole, commands.MissingPermissions]):

        await ctx.respond(
            '❌ Нет прав для использования этой команды',
            ephemeral=True
        )

    else:
        await ctx.respond(
            embed=discord.Embed(
                title='Произошла ошибка!',
                description=error,
                color=0xFF0000
            ),
            ephemeral=True
        )
        raise error


def setup(bot):
    bot.event(on_application_command_error)