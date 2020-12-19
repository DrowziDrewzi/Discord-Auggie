import discord
from discord.ext import commands
import requests
import csv
import subprocess
from subprocess import Popen, PIPE

client = commands.Bot(command_prefix = '-')
client.remove_command('help')

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))


@client.command()
async def add(ctx, repo):

    with open("csv_file.csv", 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        line = "1 " + repo
        csvwriter.writerow(line.split())

    try:
        subprocess.call(["augur", "db", "add-repos", "csv_file.csv"])
    except:
        await ctx.send("Sorry, something went wrong. Make sure your repository is public and try again.")
        print("didnt work")
    else:
        await ctx.send("Your repository has been added!")
        print("it worked")

    response = requests.get("http://localhost:5114/api/unstable/repos/22071/laborhours")
    print(response.status_code)

@client.command()
async def listgroups(ctx):
     x = requests.get('http://lions.sociallycompute.io:5100/api/unstable/repo-groups/')
     json_text = json.loads(x.text)

     for object in json_text:
             print(object["rg_name"])

@client.command()
async def list(ctx, groupID):

  x = requests.get('http://lions.sociallycompute.io:5100/api/unstable/repos/')
  json_text = json.loads(x.text)

  for object in json_text:
    if object["repo_group_id"] == int(groupID):
      repoID = str(object["repo_id"])
      repoName = str(object["repo_name"])
      description = str(object["description"])
      url = str(object["url"])
      repoStatus = str(object["repo_status"])
      commitsAllTime = str(object["commits_all_time"])
      issuesAllTime = str(object["issues_all_time"])
      rgName = str(object["rg_name"])
      repoGroupId = str(object["repo_group_id"])
      base64url = str(object["base64_url"])
      await ctx.send("Repo ID: " + repoID + "\n" + "Repo Name: " + repoName + "\n" + "Description: " + description + "\n" + "URL: " + url + "\n" + "Repo Status: " + repoStatus + "\n" + "Commits All Time: " + commitsAllTime + "\n" + "Issues All Time: " + issuesAllTime + "\n" + "RG Name: " + rgName + "\n" + "Repo Group ID: " + repoGroupId + "\n" + "Base64 URL: " + base64url)

@client.command()
async def help(ctx):
    embed = discord.Embed(
        colour = discord.Colour.red()
    )

    embed.set_author(name='Help')
    embed.add_field(name='-request-data <repo link>', value='Gives back data about repo by providing link to repo', inline=False)
    embed.add_field(name='-add-repo <repo link>', value='Adds repo to our repo database that the bot will regularly check to provide updates', inline=False)
    embed.add_field(name='-schedule <frequency>', value='Specify scheduled message time. Options are: daily, weekly, or monthly', inline=False)
    embed.add_field(name='-list <repo group ID>', value='Returns list of repos belonging to a specified repo group', inline=False)

    await ctx.send(embed=embed)

client.run(<TOKEN>)
