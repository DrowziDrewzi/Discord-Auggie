import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '-')
client.remove_command('help')

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))


@client.command()
async def hello(ctx):
    await ctx.send('world!')

@client.command()
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.red()
    )

    embed.set_author(name='Help')
    embed.add_field(name='-request-data <repo link>', value='Gives back data about repo by providing link to repo', inline=False)
    embed.add_field(name='-add-repo <repo link>', value='Adds repo to our repo database that the bot will regularly check to provide updates', inline=False)
    embed.add_field(name='-schedule <frequency>', value='Specify scheduled message time. Options are: daily, weekly, or monthly', inline=False)
    embed.add_field(name='-list', value='Returns list of repos you are following', inline=False)


    await ctx.author.send(author, embed=embed)

client.run('Nzc4ODMwNTA2MTcwOTA4NzEy.X7Xsbg.Wixyy2VJKcVI7YXAqjTeYJ8vQ_w')
