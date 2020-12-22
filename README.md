# Discord-Auggie
We are integrating Augur to be used with Discord, and we want to focus on returning the activity metrics of repos to the user. We plan on having a list of repos for the bot to return metrics for. We plan for the user to be able to schedule a regular time for the bot to send the metrics for these repos. The user will instruct the bot through commands; we currently have 5 commands..   

The user will be assisted with using the bot through the “-help” command. We can also allow the bot to respond to any direct message which does not include a command with the same response it gives for the “-help” command, for cases in which the user does not know the help command.

Rather than creating a fork of Augur, we created our own repository through which we will expand upon Discord-Auggie. We will use Augur’s Auggie (https://github.com/chaoss/augur-auggie) as a starting point. The development process will involve some reconfiguration of the original Auggie, as well as the integration of new commands. 


Distribution of work on commands:
- Drew: monitor command
- Brenna: schedule command
- Tarek: list command
- Huzaifa: look command

# How to use Discord-Auggie: 
follow this link to add discord-auggie to a discord server!

https://discord.com/api/oauth2/authorize?client_id=779124634318536735&permissions=2048&scope=bot

Now that the bot is in your server you can use these commands: 

- "-help": gives user list of all commands
- "-list <repo group ID>": will return a list of repos belonging to a specified repo group.
- "-look <repo ID>: returns all info on repo if it exists.
- "-listgroups" returns list of all stored repo groups in augur
- "-monitor <repo group ID>": adds repo to the list of repos the user wishes to monitor.
- "-schedule <frequency>": use daily, weekly, or monthly as your option to have the timed messages sent. 

The general idea is that the user should use list, look, and listgroups to decide which groups they want to monitor and then use monitor to add them to their list. Once the repos are added that user will recieve messages about those repo groups when they use the schedule command on their timed interval (daily, weekly, montly). 

# A more in-depth look at how the commands work
list <repo_group_id>

- The Discord user sends the “-list” command followed by the repo_group_id. The program retrieves a list of all stored repositories using the JSON file at “http://lions.sociallycompute.io:5100/api/unstable/repos/“. Then, the program uses a for-loop to find and display all JSON objects (repositories) with a repo_group_id matching the ID supplied by the user. 

listgroups

- The Discord user sends the “-listgroups” command. The program retrieves a list of all stored repo groups using the JSON file at “http://lions.sociallycompute.io:5114/api/unstable/repo-groups/“. Then, the program uses a for-loop to display all JSON objects (repo groups). (*NOTE: The program excludes an extra group we added but could not remove, which causes errors. On other servers where repo groups are added correctly, this would not be an issue.)

mygroups

- The Discord user sends the “-mygroups” command. The program retrieves the user’s username and Discord tag using Discord’s client, and uses that information to access a text file with a list of all stored repo group IDs.  (This text file can be created and added onto with the “-monitor” command.)Then, the program uses a for-loop to display all of the repo group IDs stored in that file. 

look <repo_id>

- The Discord user sends the “-look” command followed by a the repo_id. The program retrieves a list of all stored repositories using the JSON file at “http://lions.sociallycompute.io:5100/api/unstable/repos/“. Then, the program uses a for-loop to find and display the JSON object (repository) with the repo_id matching the ID supplied by the user. 

monitor <repo_group_id>

- The Discord user sends the “-monitor” command followed by the repo_group_id. The program retrieves the user’s username and Discord tag using Discord’s client, and then uses that to access a text file named after this information. If the file does not already exist, then it is created. The program checks if the repo_group_id is already being monitored by comparing the user’s input to each line in the text file. Then, the program accesses a list of all stored repo groups using the JSON file at “http://lions.sociallycompute.io:5114/api/unstable/repo-groups/”. Using the JSON data, the program checks if the repo_group_id exists. If the repo_group_id exists in the JSON file but not in the user’s text file, then it is added to the monitoring list.

schedule <frequency>

- The Discord user sends the “-schedule” command followed by the frequency with which they would like to receive updates. They can choose to receive updates daily (every 24 hours), weekly (every 168 hours), or monthly (every 730 hours).  The bot checks if the user input the command properly, then checks if there is already a schedule function running. Then, it starts a task by calling one of the schedule functions(daily_schedule, weekly_schedule, or monthly_schedule.) Each function runs at different increments of time. When any of the functions are called, they call another function which collects data about the repo groups from the user’s monitor list.
