import discord
from discord.ext import commands, tasks
import requests
import json

client = commands.Bot(command_prefix = '-')
client.remove_command('help')

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))

@client.command()
async def listgroups(ctx):
    x = requests.get('http://lions.sociallycompute.io:5114/api/unstable/repo-groups/')
    json_text = json.loads(x.text)

    embed = discord.Embed(title = "List of All Repo Groups", colour = discord.Colour.red())

    i = 1
    for object in json_text:
        if object["repo_group_id"] == 12:
            continue
        embed.add_field(name = str(i) + ". " + str(object["rg_name"]), value = "Repo Group ID: " + str(object["repo_group_id"]), inline = False)
        i += 1

    await ctx.send(embed=embed)

@client.command()
async def mygroups(ctx):
    user = ctx.message.author

    try:
        f = open(str(user)+".txt", "r")
        repo_groups = []

        for line in f:
            repo_groups.append(line)

        f.close()

        if not repo_groups:
            await ctx.send("Currently, you have an empty list. You need to use -monitor to add at least one repo group to monitor.")
            return

        i = 1
        embed = discord.Embed(title = str(user) +"'s Repo Groups", color = discord.Colour.red())
        for repo in repo_groups:
            embed.add_field(name = str(i), value = str(repo))
            i += 1

        await ctx.send(embed=embed)

    except:
        await ctx.send("Make sure you have already used the -monitor command to create a file.")

@client.command()
async def list(ctx, groupID):

    x = requests.get('http://lions.sociallycompute.io:5100/api/unstable/repos/')
    json_text = json.loads(x.text)

    for object in json_text:
        if object["repo_group_id"] == int(groupID):
            embed = discord.Embed(title = str(object["repo_name"]), color = discord.Colour.red())
            embed.add_field(name = "Repo ID: ", value = str(object["repo_id"]), inline=True)
            embed.add_field(name = "Description: ", value = str(object["description"]), inline=True)
            embed.add_field(name = "URL: ", value = str(object["url"]), inline=True)
            embed.add_field(name = "Repo Status: ", value = str(object["repo_status"]), inline=True)
            embed.add_field(name = "Commits All Time: ", value = str(object["commits_all_time"]), inline=True)
            embed.add_field(name = "Issues All Time: ", value = str(object["issues_all_time"]), inline=True)
            embed.add_field(name = "Repo Group Name: ", value = str(object["rg_name"]), inline=True)
            embed.add_field(name = "Repo Group ID: ", value = str(object["repo_group_id"]), inline=True)
            embed.add_field(name = "Base64 URL: ", value = str(object["base64_url"]), inline=True)
            await ctx.send(embed=embed)

@client.command()
async def help(ctx):
    embed = discord.Embed(
        colour = discord.Colour.red()
    )

    embed.set_author(name='Help')
    embed.add_field(name='-monitor <repo group ID>', value='Adds repo group to a list of repo groups associated with your user. You will monitor these when you use the -schedule command.', inline=False)
    embed.add_field(name='-schedule <frequency>', value='Schedules a regular time when you will recieve messages about your monitored repo groups. Options are: daily, weekly, or monthly.', inline=False)
    embed.add_field(name='-listgroups', value='Returns list of all stored repo groups.', inline=False)
    embed.add_field(name='-mygroups', value='Returns list of repo groups being monitored by your user.', inline=False)
    embed.add_field(name='-list <repo group ID>', value='Returns list of repos belonging to a specified repo group', inline=False)
    embed.add_field(name='-look <repo ID>', value='Returns all information regarding the repository, if it exists.', inline = False)
    await ctx.send(embed=embed)

@client.command()
async def monitor(ctx, groupID):
    user = ctx.message.author

    x = requests.get('http://lions.sociallycompute.io:5114/api/unstable/repo-groups/')
    json_text = json.loads(x.text)
    found_repo = False

    f=open(str(user)+".txt", "a+")
    f.close()

    try:
        f = open(str(user)+".txt", "r")
        i = 0
        for line in f:
            print(line + " and " + groupID)
            if int(line) == int(groupID):
                await ctx.send("repo group is already being monitored!")
                f.close()
                return
    except ValueError:
        await ctx.send("please input a valid number for repo group ID")
        f.close()
        return
    f.close()

    f = open(str(user)+".txt", "a+")
    try:
        for object in json_text:
            if object["repo_group_id"] == int(groupID):
                found_repo = True
                repo_group_name = object["rg_name"]
                await ctx.send("found repo group, name is " + repo_group_name)
                f.write(str(object["repo_group_id"])+"\n")
        if found_repo == False:
            await ctx.send("repo not found")

    except ValueError:
        await ctx.send("please input a valid number for repo group ID")

    f.close()

async def find_data(ctx, user):
    i = 0
    links = []
    f=open(str(user)+".txt", "r")
    for line in f:
        link = 'http://lions.sociallycompute.io:5114/api/unstable/repo-groups/' + line + '/top-insights'
        links.append(link)
    f.close()

    try:
        for link in links:
            repo_dict = {}
            x = requests.get(link)
            json_text = json.loads(x.text)

            if len(json_text) == 0:
                continue

            for object in json_text:
                repo_group_name = object["rg_name"]
                break

            for object in json_text:
                if object["repo_id"] in repo_dict:
                    continue
                else:
                    repo_dict[str(object["repo_id"])] = object["repo_git"]

            req = requests.get('http://lions.sociallycompute.io:5114/api/unstable/repos/')
            repos = json.loads(req.text)

            embedTitle = discord.Embed(title = str("Updates for " + repo_group_name), color = discord.Colour.red())
            await ctx.send(embed=embedTitle)

            for repo_id, repo_git in repo_dict.items():
                for repo in repos:
                    if (repo['repo_id'] == int(repo_id)):
                        embed = discord.Embed(title = str(repo['repo_name']), color = discord.Colour.dark_grey())
                        embed.add_field(name='URL',value=str(repo['url']) ,inline= True)
                        embed.add_field(name='Repository Status', value = str(repo['repo_status']), inline = True)
                        embed.add_field(name='Repository Description', value = str(repo['description']), inline=False)
                        embed.add_field(name = 'All Time Commits', value = str(repo['commits_all_time']), inline = False)
                        embed.add_field(name = 'All Time Issues', value = str(repo['issues_all_time']), inline=True)
                        embed.add_field(name = 'RGName', value = str(repo['rg_name']), inline=True)
                        embed.add_field(name = 'Group ID', value = str(repo['repo_group_id']), inline = True)
                        embed.add_field(name = 'Base64URL', value = str(repo['base64_url']), inline = True)
                        break

                replace_repo_git = repo_git.replace("/", "%2F")
                update_link = "http://lions.sociallycompute.io/repo/" + repo_group_name + "/" + replace_repo_git + "/overview"
                embed.add_field(name = 'All updates:', value = str(update_link), inline = False)
                await ctx.send(embed=embed)

        await ctx.send(user.mention)

    except:
        await ctx.send(user.mention + "There was an error when monitoring your repo group(s).")


@tasks.loop(hours = 24)
async def daily_schedule(ctx, user):
    await find_data(ctx, user)

@tasks.loop(hours = 168)
async def weekly_schedule(ctx, user):
    await find_data(ctx, user)

@tasks.loop(hours= 730)
async def monthly_schedule(ctx, user):
    await find_data(ctx, user)

@client.command()
async def schedule(ctx, frequency):
    user = ctx.message.author

    try:
        f = open(str(user)+".txt", "r")
        f.close()
    except:
        await ctx.send("Please add repo groups to monitor with -monitor before using the -schedule command.")
        return

    try:
        if frequency == "daily":
            if daily_schedule.is_running():
                await ctx.send("This schedule has already been set.")
                return
            if weekly_schedule.is_running():
                weekly_schedule.stop()
            if monthly_schedule.is_running():
                monthly_schedule.stop()

            await ctx.send("Updates for your repo group(s) will be sent to this channel daily.")
            await daily_schedule.start(ctx, user)

        elif frequency == "weekly":
            if daily_schedule.is_running():
                daily_schedule.stop()
            if weekly_schedule.is_running():
                await ctx.send("This schedule has already been set.")
                return
            if monthly_schedule.is_running():
                monthly_schedule.stop()

            await ctx.send("Updates for your repo group(s) will be sent to this channel weekly.")
            await weekly_schedule.start(ctx, user)

        elif frequency == "monthly":
            if daily_schedule.is_running():
                daily_schedule.stop()
            if weekly_schedule.is_running():
                weekly_schedule.stop()
            if monthly_schedule.is_running():
                await ctx.send("This schedule has already been set.")
                return

            await ctx.send("Updates for your repo group(s) will be sent to this channel monthly.")
            await monthly_schedule.start(ctx, user)

        else:
            await ctx.send("Please choose daily, weekly, monthly.")
    except:
        await ctx.send("Something went wrong, please try again.")


@client.command()
async def look(ctx, repo_id):
   # await ctx.send("testing")
   req = requests.get('http://lions.sociallycompute.io:5114/api/unstable/repos/')
   repos = json.loads(req.text)

   for repo in repos:
       if (repo['repo_id'] == int(repo_id)):

           embed = discord.Embed(
                   color = discord.Colour.blue()
                   )
           embed.set_author(name=str(repo['repo_name']))
           embed.add_field(name='URL',value=str(repo['url']) ,inline= True)
           embed.add_field(name='URL',value=str(repo['url']) ,inline= True)
           embed.add_field(name='Repository Status', value = str(repo['repo_status']), inline = True)
           embed.add_field(name='Repository Description', value = str(repo['description']), inline=False)
           embed.add_field(name = 'All Time Commits', value = str(repo['commits_all_time']), inline = False)
           embed.add_field(name = 'All Time Issues', value = str(repo['issues_all_time']), inline=True)
           embed.add_field(name = 'RGName', value = str(repo['rg_name']), inline=True)
           embed.add_field(name = 'Group ID', value = str(repo['repo_group_id']), inline = True)
           embed.add_field(name = 'Base64URL', value = str(repo['base64_url']), inline = True)
           await ctx.send(embed=embed)
           return
   await ctx.send("repo not found")


client.run(<BOT-TOKEN>)
