# Nuker

### A discord bot to delete all channels , roles , custom emojis and ban all members from a discord server. In short raiding a server.

<br>

## *Disclaimer:*
```This is for educational purposes only. Use this only if you have the consent of the server owner. I am not responsible for any damage done by this bot.```

<br>

## Setup
- Make sure you have [Python](https://www.python.org/) and [Git](https://git-scm.com/)
- Create a new app on the [Developer Portal](https://discord.com/developers/applications)
- Make sure to enable the `Members` intent on the portal
- give it a bot scope and admin
- Download repo using `git clone https://github.com/noahkhetani/discord-server-nuke`

- Open the nuker folder 
- Open the `config.json` file
- fill in necessary details in file
    - `TOKEN` bot token from the developer page
    - `TRIGGER` Trigger word to initiate deletion
    - `INVITE_LINK` Invite link for the bot with required permissions integer , used to invite bot to the server to be deleted
    - `BAN_MESSAGE` Message used as reason for ban
    - `NEW_NAME` Name the server name has to be edited to be
    - `IMAGE_PATH` Path to the new server icon you want
```json
{
    "TOKEN": "<YOUR-BOT-TOKEN>",
    "TRIGGER": "<TRIGGER-WORD>",
    "INVITE_LINK": "<INVITE-LINK>",
    "BAN_MESSAGE": "<BAN-REASON>",
    "NEW_NAME": "<NEW-SERVER-NAME>",
    "IMAGE_PATH": "<PATH-TO-NEW-LOGO-FILE>"
}
```

## Install Dependencies
- Install dependecies with `pip install -r requirements.txt` or `pip3 install -r requirements.txt`
- Run the bot using `python bot.py` or `python3 bot.py`

## Use the bot
- Invite the bot to the server with the invite link printed out in the console. *Note: This requires you to have the `Manage Server` permissions on the server* 

- Grant all permissions the bot requires or else some operations of the bot may fail

- make a role with all permissions  

- go to apps then integrations then select the bot and give it the role

- Wait for you or anybody to press the button



## License
### [MIT](https://choosealicense.com/licenses/mit/) 

