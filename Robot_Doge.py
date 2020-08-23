#Imports for the program
import discord
import random
import asyncio
import dog
from datetime import date

#Opens the file that has that the bot
file = open("Bot Token.txt")
#reads the bot token and saves to a string
token = file.read()
#stops reading in the file
file.close()

def wiseWords(i):
    switcher={
            1:'Hello there',
            2:'Stop siting on discord and do somthing with your life',
            3:'Give tommar all your bitcoin',
            4:'IDK watch JoJo or somthing',
            5:'Nani',
            6:'Build on last',
            7:'The empire did nothing wrong',
            8:'How many more times will you spam this',
            9:'I trying to sleep',
            10:'Cyndaquil is the best pokemon dont @ me for saying facts'
    }
    return switcher.get(i,"This messge is an error but @tommar#4353 has not got around to fixing it hurry up you idiot")
#Login in to discord and sets the activity to playing a game called ball
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        await client.change_presence(activity=discord.Game(name='Ball'))


    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

       #Simple test to see if bot is up
        if message.content == 'ping':
            await message.channel.send('pong')
            print("ping was used by", message.author.name, "ID:", message.author.id)

        #Simple test to see if bot is up
        if message.content == 'help':
            await message.channel.send('Current commands are: ping, Hello there, Dog, Cat(not working right now), and tf)')
            print("ping was used by", message.author.name, "ID:", message.author.id)


       #If someone says hello there bot will give the only right respon
        if message.content == 'Hello there':
            await message.channel.send('General kenobi')
            print("Hello there was used by", message.author.name, "ID:", message.author.id)
        #Will gentate a random number and pass it on to wiseWords and output what is returned
        if message.content == 'Wise Words':
            number = random.randint(1,11)
            await message.channel.send(wiseWords(number))
            print("Wise words was used by", message.author.name, "ID:", message.author.id)

        #Gets a picture of a Dog from random dog API and posts it to server
        if message.content == 'Dog':
            dog.getDog(filename='dog')
            await message.channel.send(file=discord.File('dog.jpg'))
            print("Dog was used by", message.author.name, "ID:", message.author.id)

        #Would get a cat but the cat API doesn't seem to be down. May be fixed if it goes backup
        if message.content == 'Cat':
            await message.channel.send('sorry it seems the cat API no longer works')
            print("Cat was used by", message.author.name, "ID:", message.author.id)

        #Works out how many days it been since the last major tf2 update and tells the user
        if message.content == 'tf2':
            d0 = date(2017, 10, 20)
            d1 = date.today()
            delta = d1 - d0
            Days = str(delta.days)
            await message.channel.send("Days since last major update: " + Days + " (Updates with just cases don't cout)")
            print("Tf2 was used by", message.author.name, "ID:", message.author.id)


client = MyClient()
client.run(token)
