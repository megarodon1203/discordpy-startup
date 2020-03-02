from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('うんこ')


bot.run(token)

@client.event
async def on_member_join(member):
    reply = f'{message.author.mention} いらっしゃい' # 返信メッセージの作成
        await message.channel.send(reply) # 返信メッセージを送信
