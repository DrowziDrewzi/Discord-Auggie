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
"-help": gives user list of all commands
"-list <repo group ID>": will return a list of repos belonging to a specified repo group.
"-look <repo ID>: returns all info on repo if it exists.
"-listgroups" returns list of all stored repo groups in augur
"-monitor <repo group ID>": adds repo to the list of repos the user wishes to monitor.
"-schedule <frequency>": use daily, weekly, or monthly as your option to have the timed messages sent. 

The general idea is that the user should use list, look, and listgroups to decide which groups they want to monitor and then use monitor to add them to their list. Once the repos are added that user will recieve messages about those repo groups when they use the schedule command on their timed interval (daily, weekly, montly). 
