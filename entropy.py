import selfcord
import sys
from selfcord.ext import commands
from typing import Optional

# token
token = 'token_here'

bot = commands.Bot(command_prefix='.', self_bot=True)

print('entropy started, waiting to login')

@bot.event
async def on_ready():
    print(f'logged in as {bot.user}')

@bot.event
async def on_command_error(error):
    if isinstance(error, commands.CommandInvokeError):
        print('dm/channel not found, make sure the dm is open or you have access to the channel')
        return
    raise error

@bot.event
async def on_error(error):
    if isinstance(error, selfcord.NotFound):
        print('dm/channel not found, make sure the dm is open or you have access to the channel')
        return
    raise error

# purge messages from bottom to top
# .p (will use current channel) OR .p snowflake (dm/group/channel)
@bot.command()
async def p(ctx, channel: Optional[int]):
    try:
        counter = 0
        await ctx.message.delete()
        if channel:
            try:
                channel_id = await bot.fetch_channel(channel)
                if channel_id:
                    async for msg in channel_id.history(limit=None):
                        if msg.author == ctx.author and (msg.type == selfcord.MessageType.default or msg.type == selfcord.MessageType.reply or msg.type == selfcord.MessageType.pins_add):
                            counter += 1
                            print(f'[{counter} deleted] {msg.content or "unknown msg"}')
                            await msg.delete()
            except selfcord.errors.NotFound:
                user = await bot.fetch_user(channel)
                if user:
                    async for msg in user.dm_channel.history(limit=None):
                        if msg.author == ctx.author and (msg.type == selfcord.MessageType.default or msg.type == selfcord.MessageType.reply or msg.type == selfcord.MessageType.pins_add):
                            counter += 1
                            print(f'[{counter} deleted] {msg.content or "unknown msg"}')
                            await msg.delete()
        else:
            async for msg in ctx.channel.history(limit=None):
                if msg.author == ctx.author and (msg.type == selfcord.MessageType.default or msg.type == selfcord.MessageType.reply or msg.type == selfcord.MessageType.pins_add):
                    counter += 1
                    print(f'[{counter} deleted] {msg.content or "unknown msg"}')
                    await msg.delete()
    except Exception as e:
        print(f'error on line {sys.exc_info()[-1].tb_lineno}', type(e).__name__, e)

# purge messages from top to bottom
# .pold (will use current channel) OR .pold snowflake (dm/group/channel)
@bot.command()
async def pold(ctx, channel: Optional[int]):
    try:
        counter = 0
        await ctx.message.delete()
        if channel:
            try:
                channel_id = await bot.fetch_channel(channel)
                if channel_id:
                    async for msg in channel_id.history(limit=None, oldest_first=True):
                        if msg.author == ctx.author and (msg.type == selfcord.MessageType.default or msg.type == selfcord.MessageType.reply or msg.type == selfcord.MessageType.pins_add):
                            counter += 1
                            print(f'[{counter} deleted] {msg.content or "unknown msg"}')
                            await msg.delete()
            except selfcord.errors.NotFound:
                user = await bot.fetch_user(channel)
                if user:
                    async for msg in user.dm_channel.history(limit=None, oldest_first=True):
                        if msg.author == ctx.author and (msg.type == selfcord.MessageType.default or msg.type == selfcord.MessageType.reply or msg.type == selfcord.MessageType.pins_add):
                            counter += 1
                            print(f'[{counter} deleted] {msg.content or "unknown msg"}')
                            await msg.delete()
        else:
            async for msg in ctx.channel.history(limit=None, oldest_first=True):
                if msg.author == ctx.author and (msg.type == selfcord.MessageType.default or msg.type == selfcord.MessageType.reply or msg.type == selfcord.MessageType.pins_add):
                    counter += 1
                    print(f'[{counter} deleted] {msg.content or "unknown msg"}')
                    await msg.delete()
    except Exception as e:
        print(f'error on line {sys.exc_info()[-1].tb_lineno}', type(e).__name__, e)

# purge messages before snowflake (message id, e.g: 1049011454973579274) - will not delete the message id used if it's yours
# .pbefore channel snowflake
@bot.command()
async def pbefore(ctx, channel: int, before: int):
    try:
        counter = 0
        await ctx.message.delete()
        if channel:
            try:
                channel_id = await bot.fetch_channel(channel)
                if channel_id:
                    async for msg in channel_id.history(limit=None, before=selfcord.utils.snowflake_time(before)):
                        if msg.author == ctx.author and (msg.type == selfcord.MessageType.default or msg.type == selfcord.MessageType.reply or msg.type == selfcord.MessageType.pins_add):
                            counter += 1
                            print(f'[{counter} deleted] {msg.content or "unknown msg"}')
                            await msg.delete()
            except selfcord.errors.NotFound:
                user = await bot.fetch_user(channel)
                if user:
                    async for msg in user.dm_channel.history(limit=None, before=selfcord.utils.snowflake_time(before)):
                        if msg.author == ctx.author and (msg.type == selfcord.MessageType.default or msg.type == selfcord.MessageType.reply or msg.type == selfcord.MessageType.pins_add):
                            counter += 1
                            print(f'[{counter} deleted] {msg.content or "unknown msg"}')
                            await msg.delete()
    except Exception as e:
        print(f'error on line {sys.exc_info()[-1].tb_lineno}', type(e).__name__, e)

# purge messages after snowflake (message id, e.g: 1049011454973579274) - will not delete the message id used if it's yours
# .pafter channel snowflake
@bot.command()
async def pafter(ctx, channel: int, after: int):
    try:
        counter = 0
        await ctx.message.delete()
        if channel:
            try:
                channel_id = await bot.fetch_channel(channel)
                if channel_id:
                    async for msg in channel_id.history(limit=None, after=selfcord.utils.snowflake_time(after)):
                        if msg.author == ctx.author and (msg.type == selfcord.MessageType.default or msg.type == selfcord.MessageType.reply or msg.type == selfcord.MessageType.pins_add):
                            counter += 1
                            print(f'[{counter} deleted] {msg.content or "unknown msg"}')
                            await msg.delete()
            except selfcord.errors.NotFound:
                user = await bot.fetch_user(channel)
                if user:
                    async for msg in user.dm_channel.history(limit=None, after=selfcord.utils.snowflake_time(after)):
                        if msg.author == ctx.author and (msg.type == selfcord.MessageType.default or msg.type == selfcord.MessageType.reply or msg.type == selfcord.MessageType.pins_add):
                            counter += 1
                            print(f'[{counter} deleted] {msg.content or "unknown msg"}')
                            await msg.delete()
    except Exception as e:
        print(f'error on line {sys.exc_info()[-1].tb_lineno}', type(e).__name__, e)

# purge messages between snowflakes (message id, e.g: 1049011454973579274) - will not delete the message id used if it's yours
# .pinbetween channel snowflake1 snowflake2
@bot.command()
async def pinbetween(ctx, channel: int, before: int, after: int):
    try:
        counter = 0
        await ctx.message.delete()
        if channel:
            try:
                channel_id = await bot.fetch_channel(channel)
                if channel_id:
                    async for msg in channel_id.history(limit=None, before=selfcord.utils.snowflake_time(before), after=selfcord.utils.snowflake_time(after)):
                        if msg.author == ctx.author and (msg.type == selfcord.MessageType.default or msg.type == selfcord.MessageType.reply or msg.type == selfcord.MessageType.pins_add):
                            counter += 1
                            print(f'[{counter} deleted] {msg.content or "unknown msg"}')
                            await msg.delete()
            except selfcord.errors.NotFound:
                user = await bot.fetch_user(channel)
                if user:
                    async for msg in user.dm_channel.history(limit=None, before=selfcord.utils.snowflake_time(before), after=selfcord.utils.snowflake_time(after)):
                        if msg.author == ctx.author and (msg.type == selfcord.MessageType.default or msg.type == selfcord.MessageType.reply or msg.type == selfcord.MessageType.pins_add):
                            counter += 1
                            print(f'[{counter} deleted] {msg.content or "unknown msg"}')
                            await msg.delete()
    except Exception as e:
        print(f'error on line {sys.exc_info()[-1].tb_lineno}', type(e).__name__, e)

bot.run(token)
