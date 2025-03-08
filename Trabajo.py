import os
import discord
from discord.ext import commands
from model import predict

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix = "#", intents=intents )

@bot.event
async def in_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def cheeck(ctx):
    if ctx.message.attachments:
        for archivo in ctx.message.attachments:
            file_name = archivo.filename
            file_url = archivo.url
            await archivo.save(f"Image/{file_name}")
            await ctx.send(predict(model_path="./keras_model.h5", labels_path="./labels.txt", image_path=f"Image/{file_name}"))

    else:
        await ctx.send("No se ha adjuntado ningun archivo")

          

bot.run("¡Pon tu token aquí!")
