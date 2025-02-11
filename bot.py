import discord
import os
import random

from bot_logic import gen_pass
from bot_logic import flip_coin
from bot_logic import get_duck_image_url
from bot_logic import get_dog_image_url
from discord.ext import commands 

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}') 

@bot.command()
async def hello(ctx):
    await ctx.send("Hi!")

@bot.command()
async def bye(ctx):
    await ctx.send("Cya")

@bot.command()
async def password(ctx, pass_length: int):
    await ctx.send(gen_pass(pass_length))

@bot.command()
async def seal(ctx):
    await ctx.send("https://tenor.com/view/huzz-seal-hi-sealutation-gif-14368511881377374735")

@bot.command()
async def meme(ctx):
    random_meme = random.choice(os.listdir('images'))
    with open(f'images/{random_meme}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def luckmeme(ctx):
    # Algunos memes tendran menos probabilidades que otros
    luck_factor = random.randint(1, 1000)
    if luck_factor == 1:
        await ctx.send("https://cdn.discordapp.com/attachments/1137649615840227390/1339014802357620756/caption.jpg?ex=67ad2e36&is=67abdcb6&hm=4b32e7e72beb824ff1f13e1441593cb533037ec960530ceeb82db444d1af118e&")
    elif luck_factor >= 2 and luck_factor <= 126:
        await ctx.send("https://cdn.discordapp.com/attachments/1137649615840227390/1339015887625261116/caption.png?ex=67ad2f39&is=67abddb9&hm=11bfbe5b9438e69771c650534b604e7e984834c2f55561ddee08bc13099752d2&")
    elif luck_factor >= 127 and luck_factor <= 627:
        await ctx.send("https://cdn.discordapp.com/attachments/1137649615840227390/1339017190015373382/caption.png?ex=67ad306f&is=67abdeef&hm=b8cf761dbb90ae1cf5630544592bcca5f13de576f4b7262089185cdaba34c79f&")
    else:
        await ctx.send("no meme :pensive:")

# Lista de APIs
@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command('dog')
async def dog(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)



bot.run("token here")