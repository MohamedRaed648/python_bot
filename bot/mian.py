import discord
from discord import message
import requests
import random
import json
from import_json import DataBase

#bot_code
token='ODY2NDE5NDkyODQyMzczMTQw.YPSSCA.VgzsZECQWnffFuDAAcKb9CfIcaQ'

client = discord.Client()

sad_words=["sad", "depressed", "unhappy", "angry", "miserable"]

starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person / bot!"
]



def get_qoute():
    request=requests.get("https://zenquotes.io/api/random")
    respone=json.loads(request.text)
    quote=respone[0]['q'] + " -" + respone[0]['a']
    return quote


def update_enc(new_enc):
    db=DataBase('locker_database','tyio1245')
    starter_encouragements.append(new_enc)
    db.Excute_upd(starter_encouragements,21)
 

    
@client.event
async def on_ready():
    print(client)

    print('We have logged in as {0.user}'.format(client))



@client.event
async def on_message(message):
    print(client.user)
    if message.author == client.user:
        return
    msg=message.content

    if msg in sad_words:
        await message.channel.send(random.choice(starter_encouragements))

    if message.content.startswith('$hello'):
        qoute=get_qoute()
        await message.channel.send(qoute)


    if message.content.startswith('$new'):
        print(message.content.split('$new')[1])
        update_enc(message.content.split('$new')[1])


# Async IO in Python: A Complete Walkthrough

client.run(token) 
