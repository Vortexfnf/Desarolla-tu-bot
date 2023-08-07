import datetime
import os
import discord
import asyncio
import random
from discord.ext import commands

# Intents
intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'The bot has logged in on discord as {client.user}')

# Ideas para ayudar contra la contamimación
ideas = [
    "Transformar botellas de plástico en PLA (hilo para impresoras 3D)",
    "Llevar plástico a centros de reciclaje locales",
    "Crear eco-ladrillos con plástico compactado",
    "Crear objetos útiles o decorativos a partir de botellas y envases plásticos",
    "Construir un invernadero pequeño utilizando botellas plásticas",
    "Usar bolsas reutilizables en lugar de bolsas plásticas de un solo uso",
    "Convertir objetos plásticos viejos en nuevos productos útiles",
    "Comprar productos con menos envases plásticos y usar contenedores recargables",
    "Informar a otros sobre la importancia del reciclaje de plástico y la reducción de su uso"
    "Utilizar plásticos biodegradables y compostarlos en lugar de desecharlos",
    "Reciclar papel y combinarlo con plástico derretido para hacer papel reciclado",
    "Cultivar tus propias frutas y verduras puede reducir el uso de envases plásticos",
    "Optar por productos reutilizables en lugar de los de un solo uso",
    "Elegir productos sin microesferas de plástico",
    "Arreglar objetos plásticos rotos en lugar de reemplazarlos",
    "Comprar productos con envases que puedan ser devueltos o rellenados",
    "Participar en limpiezas comunitarias para eliminar plásticos de entornos naturales",
    "Optar por opciones reutilizables o biodegradables",
    "Apoyar iniciativas y legislaciones locales para reducir el uso de plásticos",
    "Promover la conciencia y la acción sostenible en la comunidad"
]

@client.command()
async def Ideas(ctx):
    print(random.choice(ideas))
    await ctx.send(random.choice(ideas))

@client.command()
async def Bidon(ctx, color="None"):
    if color.upper() == "AMARILLO":
        await ctx.send("Bidón Amarillo: Para reciclar envases")
    elif color.upper() == "AZUL":
        await ctx.send("Bidón Azul: Para reciclar Papel y Cartón")
    elif color.upper() == "GRIS":
        await ctx.send("Bidón Gris: Para reciclar Papel y Cartón")
    elif color.upper() == "VERDE":
        await ctx.send("Bidón Verde: Para reciclar Vidrio")
    elif color.upper() == "ROJO":
        await ctx.send("Bidón Rojo: Para reciclar Plástico")
    elif color.upper() == "MARRON":
        await ctx.send("Bidón Marrón: Para reciclar Materia Orgánica")
    elif color.upper() == "NEGRO":
        await ctx.send("Bidón Negro: Para residuos no reciclables")
    else:
        await ctx.send("Color de Bidón no reconocido. Por favor, elija entre: Amarillo, Azul, Gris, Verde, Rojo, Marrón o Negro.")
    

@client.command(name="server_info", aliases=["serverinfo"], help="Displays information about the server.")
async def server_info(ctx):
    # Get the server information
    server = ctx.guild
    # Creating an embed
    embed = discord.Embed(title="Server Information", color=discord.Color.blue())
    
    embed = discord.Embed(title=f"Server Information - {server.name}", color=discord.Color.blue())
    embed.set_thumbnail(url=server.icon.url)  # Use 'icon' attribute instead of 'icon_url'
    embed.add_field(name="Server's ID", value=server.id, inline=False)
    embed.add_field(name="Server owner", value=server.owner, inline=False)
    embed.add_field(name="Total member count", value=server.member_count, inline=False)
    embed.add_field(name="Text channels", value=len(server.text_channels), inline=False)
    embed.add_field(name="VC's", value=len(server.voice_channels), inline=False)
    embed.add_field(name="Roles", value=len(server.roles), inline=False)

    # Send the embed message
    await ctx.send(embed=embed)

# Setting the command description for the 'server_info' command
server_info.description = "This command displays detailed information about the server."

# Setting the command brief for the 'server_info' command (a shorter description for use in the default help command)
server_info.brief = "Displays server information."

client.run("MTEyOTA5MjQ5NzIzMTA2OTI0NA.GKjAKA.XdBCh7CofcIX1arUp4DD_rb0gxgo6_kWpMzhQM")