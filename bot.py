import discord
from discord.ext.commands import Bot
import requests

bot = Bot(command_prefix='$')
TOKEN = 'discord bot token'

@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = 'CP'))
    print("online")

@bot.command(name="hwid")
async def HWIDReset(ctx, arg):

    #await ctx.send("invalid syntax, command should look like this $hwid NayNaed")

  hwidRequest = requests.get("https://www.projecthades.org/PH/includes/api/ph_api.php?action=hwid", json = {
  "client_id" : "replace with client id",
  "request" : "reset",
  "user" : arg
})

  if(hwidRequest.text == '{"success":false,"error":"Failed to reset hwid."}'):

        embedVar = discord.Embed(title="Action Failed", description="Your hwid has not been reset for one of the reasons below", color=0xFF0000)
        embedVar.add_field(name="Your HWID is not set yet", value="meaning that you need to log in to set a hwid for your account", inline=False)
                                                                                                                                                        #i would replace this since you dont want to do free advertising 
        embedVar.add_field(name="The name you provided is not valid", value="the name you have for the hwid reset is not valid, provide your name on the [get oracle website](https://getoracle.xyz/index.php)", inline=False)
        embedVar.add_field(name="Server-side issue", value="This is rare but still possible, the servers could be down at the time of this request")
        await ctx.send(embed=embedVar)

    #await ctx.send("there has been an error, eaither your hwid is already reset or there is a server side issue")

  if(hwidRequest.text == '{"success":true}'):

        embedVar = discord.Embed(title="Action Successful", description="", color=0x00ff00)
        embedVar.add_field(name="Your hwid has been reset successfully", value="Your good to go", inline=False)
        await ctx.send(embed=embedVar)

    #await ctx.send("hwid has been reset successfully")

    #await ctx.send(hwidRequest.text)

bot.run(TOKEN)
