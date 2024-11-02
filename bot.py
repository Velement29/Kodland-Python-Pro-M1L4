import discord
import random
import asyncio
from discord.ext import commands
from bot_gencontraseña import gen_pass

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot llamado {bot.user}!')

@bot.command()
async def bye(ctx):
    await ctx.send(f'Adios amigo!')

@bot.command()
async def genera_contraseña(ctx, longitud = 0):
    if longitud == 0:
        await ctx.send(f'No podemos generar una contraseña de 0 digitos. ;)')
    else:
        await ctx.send(f'Muy bien! Tu contraseña generada es: ' + gen_pass(longitud))

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

"""@bot.event
async def on_message(self, message):
    # we do not want the bot to reply to itself
    if message.author.id == self.user.id:
        return

    if message.content.startswith('$guess'):
        await message.channel.send('Guess a number between 1 and 10.')

        def is_correct(m):
            return m.author == message.author and m.content.isdigit()

        answer = random.randint(1, 10)

        try:
            guess = await self.wait_for('message', check=is_correct, timeout=5.0)
        except asyncio.TimeoutError:
            return await message.channel.send(f'Sorry, you took too long it was {answer}.')

        if int(guess.content) == answer:
            await message.channel.send('You are right!')
        else:
            await message.channel.send(f'Oops. It is actually {answer}.')"""

@bot.command()
async def adivina(ctx, numero_decidido = -1):
    numero_seleccionado = random.randint(0, 10)

    if numero_seleccionado == numero_decidido:
        await ctx.send("Muy bien! El número que adivinaste es el mismo que yo pense!")
    else:
        await ctx.send("Aw! El número que escribiste no es el mismo que yo pense! Yo pense en el número " + str(numero_seleccionado))

bot.run("MTI5OTUxMjA0NDU3NTUyMjg3Ng.GFudMf.Brb4pz0KUHln0IJMtugN4cUgv6PyXChx0J41xU")