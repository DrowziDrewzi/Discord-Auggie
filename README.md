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
