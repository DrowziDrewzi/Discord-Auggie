# Discord-Auggie
We are integrating Auggie to be used with Discord, and we want to focus on returning the activity metrics of repos to the user. We plan on having a list of repos for the bot to return metrics for, which can be expanded upon by the user. We plan for the user to be able to schedule a regular time for the bot to send the metrics for these repos. The user will instruct the bot through commands; we currently have 5 commands planned to be implemented.   

The user will be assisted with using the bot through the “-help” command. We can also allow the bot to respond to any direct message which does not include a command with the same response it gives for the “-help” command, for cases in which the user does not know the help command.

Our current plan for what Discord-Auggie should include after completion:
- Reconfigured files from chaoss/augur-auggie
- Request Repo Data command
- Add repos to list command
- Schedule times messages command
- Return user’s list of repos command

Rather than creating a fork of Augur, we created our own repository through which we will expand upon Discord-Auggie. We will use Augur’s Auggie (https://github.com/chaoss/augur-auggie) as a starting point. The development process will involve some reconfiguration of the original Auggie, as well as the integration of new commands. 

So far, we have created a simple Discord bot in order to show proof of concept for connecting to Discord’s API. We are still determining how to connect to Augur’s API; we have started working on this with the help of the original Auggie’s repository. 

Our current goals:
- Research the tradeoffs between using Python or JavaScript
    - We are more familiar with Python, but there is already a working configuration for JavaScript we can work from
- Research Discord bot creation and Discord API
- Look over Auggie’s files and research Augur’s API

Distribution of work on commands:
- Drew: Request Repo Data
- Brenna: Add repos to list
- Tarek: Schedule Timed Messages
- Huzaifa: Return users list of repos

Sprint Goals:
- Sprint 3:
    - Reconfigure Auggie to work with Discord
    - Start developing commands
- Sharing: 
    - Video will show the original Auggie’s commands working in Discord
    - We will also show where we are with developing new commands
- Sprint 4:
    - Commands function properly
    - Reevaluate original requirements and decide what can be added or changed
- Final Code:
    - Update commands based upon reevaluation in Sprint 4

- SPRINT 3 UPDATE: 
Right now, we think Auggie will work best existing outside of the Augur repository. On our server, we have two virtual environments for Augur and Discord-Auggie. In our Discord-Auggie folder, we have a bot.py file which allows us to run our bot with the use of our Discord bot’s token. At the moment we think we can set up all of our commands in this bot.py file. Our goal is for the bot to be able to respond to 5 commands. 
    - The help command is already functioning; it returns a list of the bots commands and the proper syntax for them. 
    - Two are partially completed, the add command and list command. The add command should take a user’s repository and add it to the list of repository’s Augur will track for this user. Auggie will execute a shell commands on our server - Augur’s “augur db add” command - which will add a repo for Augur to track. 
    - The list command will also execute a shell command - Augur’s “augur db group” - which will return the list of repos which are being tracked.
    - Obstacles: 
        -One obstacle we are facing right now is that we are having issues with our Augur instance. After it is fixed, we can finish implementing the add command. The      look command will be completed when we determine how to properly pass the information from the shell to our bot.The last two commands we hope to implement include the schedule command and the look command. The schedule command will help the user with scheduling when to receive updates on their repos through Discord messages, and how often to receive these updates. The look command will help a user look at the current state of a specific server they are tracking.
