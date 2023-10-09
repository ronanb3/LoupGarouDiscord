from loup_garou import *
import asyncio, discord, os
from discord.ext import commands
from discord.ui import Select, View
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
authors = []
pseudos = []
dicAuthors = {}

bot = commands.Bot(command_prefix='%', intents=intents)


# Set the confirmation message when the bot is ready
@bot.event
async def on_ready():
    ver = "1.0.0"
    lang = "fr"
    print("PlayerBot " + ver + " " + lang)

# Set the commands for your bot
@bot.command()
async def aide(ctx):
    phrase = 'Ce bot sert à tester le jeu du Loup Garou. Il simule 10 joueurs différents' 
    await ctx.send(phrase)

@bot.command()
async def voleur(ctx):
    response = 'Le voleur se réveille et donne le nom de la personne à voler'
    await ctx.send(response)
        
@bot.command()
async def test(ctx,text):
    author = ctx.message.author
    print ("test: "+ str(author.id))
    await ctx.author.send('Your ID is: ' + str(author.id))
    await ctx.author.send('Your Message is: ' + text)

# Retrieve token from the .env file
load_dotenv()
## bot.run(os.getenv('TOKEN1'))
## bot.run(os.getenv('TOKEN2'))

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
task1 = loop.create_task(bot.start(os.getenv('TOKEN1')))
task2 = loop.create_task(bot.start(os.getenv('TOKEN2')))

try:
    loop.run_forever()
except KeyboardInterrupt:
    loop.stop()
    loop.close()




    
