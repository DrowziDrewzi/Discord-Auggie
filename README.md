# Discord-Auggie
We created a new version of Auggie to be used with Discord rather than Slack. Our focus was on returning the activity metrics of repos to the user. Using the bot, the user can create a list of repo groups to recieve regular updates about from the bot. The user is able to schedule a regular time for the bot to send the metrics for these repos. The user will instruct the bot through commands. We have 5 commands, excluding the help command.

The user will be assisted with using the bot through the “-help” command. We can also allow the bot to respond to any direct message which does not include a command with the same response it gives for the “-help” command, for cases in which the user does not know the help command.

Rather than creating a fork of Augur, we created our own repository through where we expanded upon Discord-Auggie. We used Augur’s Auggie (https://github.com/chaoss/augur-auggie) as a starting point. We originally planned on reconfiguring the original Auggie, but instead we opted on building our own bot from the ground up using Python and discord.py.

Distribution of work on commands:
- Drew: monitor command
- Brenna: schedule, listgroups, mygroups command
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
list 

- The Discord user sends the “-list” command followed by the repo_group_id. The bot retrieves a list of all stored repositories using the JSON file at “http://lions.sociallycompute.io:5100/api/unstable/repos/“. Then, the bot uses a for-loop to find and display all JSON objects (repositories) with a repo_group_id matching the ID supplied by the user. 

listgroups

- The Discord user sends the “-listgroups” command. The bot retrieves a list of all stored repo groups using the JSON file at “http://lions.sociallycompute.io:5114/api/unstable/repo-groups/“. Then, the bot uses a for-loop to display all JSON objects (repo groups). (*NOTE: The bot excludes an extra group we added but could not remove, which causes errors. On other servers where repo groups are added correctly, this would not be an issue.)

mygroups

- The Discord user sends the “-mygroups” command. The bot retrieves the user’s username and Discord tag using Discord’s client, and uses that information to access a text file with a list of all stored repo group IDs.  (This text file can be created and added onto with the “-monitor” command.)Then, the bot uses a for-loop to display all of the repo group IDs stored in that file. 

look 

- The Discord user sends the “-look” command followed by a the repo_id. The bot retrieves a list of all stored repositories using the JSON file at “http://lions.sociallycompute.io:5100/api/unstable/repos/“. Then, the bot uses a for-loop to find and display the JSON object (repository) with the repo_id matching the ID supplied by the user. 

monitor

- The Discord user sends the “-monitor” command followed by the repo_group_id. The bot retrieves the user’s username and Discord tag using Discord’s client, and then uses that to access a text file named after this information. If the file does not already exist, then it is created. The bot checks if the repo_group_id is already being monitored by comparing the user’s input to each line in the text file. Then, the bot accesses a list of all stored repo groups using the JSON file at “http://lions.sociallycompute.io:5114/api/unstable/repo-groups/”. Using the JSON data, the bot checks if the repo_group_id exists. If the repo_group_id exists in the JSON file but not in the user’s text file, then it is added to the monitoring list.

schedule 

- The Discord user sends the “-schedule” command followed by the frequency with which they would like to receive updates. They can choose to receive updates daily (every 24 hours), weekly (every 168 hours), or monthly (every 730 hours).  The bot checks if the user input the command properly, then checks if there is already a schedule function running. Then, it starts a task by calling one of the schedule functions(daily_schedule, weekly_schedule, or monthly_schedule.) Each function runs at different increments of time. When any of the functions are called, they call another function(find_data) which finds insights data for each of the repo groups by accessing a JSON file using a URL containing the repo_group_id. Then, the bot posts this data for each of the repo groups (that have available insights data) listed in the user’s monitor list.
