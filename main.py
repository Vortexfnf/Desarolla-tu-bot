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
    "Informar a otros sobre la importancia del reciclaje de plástico y la reducción de su uso",
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
    "Promover la conciencia y la acción sostenible en la comunidad",
    "Fomentar el uso de botellas de agua reutilizables",
    "Utilizar pajitas de metal o bambú en lugar de pajitas de plástico",
    "Reemplazar utensilios de plástico con alternativas de acero inoxidable o madera",
    "Evitar el uso de envoltorios de plástico al transportar alimentos",
    "Comprar productos de segunda mano en lugar de nuevos para reducir el uso de embalajes",
    "Apoyar negocios locales que utilizan envases biodegradables",
    "Crear una campaña educativa sobre el impacto del plástico en los océanos",
    "Desarrollar un programa de recolección de plásticos en áreas rurales",
    "Utilizar contenedores de vidrio en lugar de plástico para almacenar alimentos",
    "Fomentar el uso de bolsas de tela para la compra de alimentos a granel",
    "Incentivar a las empresas a adoptar prácticas de embalaje sostenibles",
    "Organizar eventos de reutilización y trueque de objetos en la comunidad",
]


@client.command()
async def Ideas(ctx):
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

challenges = [
    "Use a reusable water bottle today.",
    "Pick up at least 5 pieces of trash you come across.",
    "Conserve energy by turning off lights and unplugging devices not in use.",
    "Walk, bike, or use public transport instead of driving if possible.",
    "Reduce plastic waste by avoiding single-use plastics today.",
    "Plant a tree or a plant in your backyard or a local park.",
    "Opt for paperless billing and statements for your accounts.",
    "Donate or recycle old electronics you no longer use.",
    "Switch to reusable cloth bags for groceries and shopping.",
    "Conserve water by taking shorter showers and fixing any leaks.",
    "Buy products with minimal packaging or packaging that can be recycled.",
    "Use a cloth napkin instead of disposable paper napkins.",
    "Reduce food waste by planning meals and using leftovers creatively.",
    "Switch to eco-friendly cleaning products for your home.",
    "Participate in a local beach or park cleanup event.",
    "Turn off faucets while brushing your teeth or doing dishes.",
    "Carpool with friends or colleagues to reduce vehicle emissions.",
    "Unsubscribe from unnecessary junk mail and catalogs.",
    "Make your own DIY natural air fresheners instead of using aerosols.",
    "Set up a composting system for your kitchen waste.",
    "Repair or repurpose an item instead of discarding it.",
    "Opt for digital invitations instead of paper for events.",
    "Use a refillable mug or cup for your coffee or drinks.",
    "Support local and sustainable products and businesses.",
    "Turn down your thermostat by a few degrees and wear warmer clothes.",
    "Use a reusable lunchbox or container instead of disposable ones.",
    "Avoid printing unnecessary documents and emails.",
    "Buy second-hand or vintage clothing instead of fast fashion.",
    "Contribute to an e-waste recycling program for electronics disposal.",
    "Spread awareness by sharing an environmental tip with a friend or on social media."
]

@client.command()
async def challenge(ctx):
    # Select a random challenge from the list
    random_challenge = random.choice(challenges)
    await ctx.send(f"🌱 Your daily challenge is: {random_challenge}")

general = "La contaminación se refiere a la introducción de sustancias, energía o agentes contaminantes en el medio ambiente, ya sea en el aire, el agua o el suelo, que causan efectos adversos en la salud humana, en los ecosistemas y en el equilibrio natural de los sistemas ambientales. Estas sustancias o agentes pueden ser productos químicos, partículas, radiación, microorganismos u otros elementos que, cuando están presentes en concentraciones superiores a las normales, generan alteraciones y daños en el entorno."

air_polution = "La contaminación del aire es la presencia en la atmósfera de sustancias nocivas en concentraciones que pueden tener efectos adversos en la salud de las personas, en el medio ambiente y en los ecosistemas. Estas sustancias contaminantes pueden ser de origen natural o humano y pueden provenir de diversas fuentes, como la quema de combustibles fósiles, la industria, la agricultura, el transporte y otras actividades humanas."

water_contamination = "La contaminación del agua se refiere a la introducción de sustancias nocivas o contaminantes en cuerpos de agua, como ríos, lagos, océanos, aguas subterráneas y otros recursos hídricos. Estas sustancias pueden alterar la calidad del agua y tener efectos adversos en los ecosistemas acuáticos, en la salud humana y en la disponibilidad de agua potable. La contaminación del agua puede ser causada por actividades humanas, naturales o una combinación de ambas."

soil_contamination = "La contaminación del suelo se refiere a la presencia de sustancias químicas, materiales o elementos tóxicos en el suelo en concentraciones que pueden ser perjudiciales para la salud humana, la vida vegetal, la fauna y el medio ambiente en general. Estos contaminantes pueden provenir de diversas fuentes, incluyendo actividades industriales, agrícolas, mineras, urbanas y otras actividades humanas. La contaminación del suelo puede tener efectos adversos a largo plazo en la calidad del suelo y en los ecosistemas que dependen de él."

sound_contamination = "La contaminación del sonido, también conocida como contaminación acústica o contaminación sonora, se refiere al exceso de ruido no deseado en el entorno que tiene efectos negativos en la salud humana, en la calidad de vida y en los ecosistemas. Este tipo de contaminación es causado por la presencia de sonidos indeseados y perturbadores que superan los niveles normales de tranquilidad en un área determinada."

light_contamination = "La contaminación lumínica, también conocida como contaminación lumínica o polución luminosa, se refiere al exceso de luz artificial en el entorno nocturno que interfiere con la observación del cielo estrellado, afecta a los ecosistemas naturales y tiene efectos negativos en la salud humana. Este tipo de contaminación se produce cuando hay una emisión excesiva de luz artificial en áreas urbanas y rurales, creando un brillo innecesario y no deseado en el cielo nocturno."

Thermal_Pollution = "Contaminación térmicase refiere a la contaminación térmica, que es el aumento de la temperatura en un cuerpo de agua, como ríos, lagos u océanos, debido a la descarga de agua caliente o caliente de fuentes industriales, de energía eléctrica o de otro tipo. Esta contaminación térmica puede tener efectos adversos en los ecosistemas acuáticos y en el medio ambiente en general."

Radioactive_Contamination = "Se refiere a la presencia no deseada de materiales radioactivos en el entorno. Estos materiales pueden provenir de actividades nucleares, accidentes en plantas nucleares, ensayos nucleares, entre otros, y pueden causar daño a la salud humana y al medio ambiente debido a la liberación de radiación ionizante."

Plastic_Pollution = "Se refiere a la acumulación y dispersión de productos plásticos en el entorno, especialmente en océanos, ríos y otros cuerpos de agua. Los plásticos pueden persistir en el medio ambiente durante mucho tiempo, causando daño a la vida marina, la fauna terrestre y afectando la cadena alimentaria."

Hazardous_Waste_Pollution = "Se refiere a la liberación inadecuada de residuos tóxicos, peligrosos o químicamente activos en el medio ambiente. Estos residuos pueden ser generados por industrias, hospitales y otros sectores, y si no se manejan adecuadamente, pueden causar impactos graves en la salud y el medio ambiente."

Biological_Contamination = "Se refiere a la introducción no deseada de microorganismos, patógenos u organismos invasores en un ecosistema. Esto puede alterar los equilibrios ecológicos y tener efectos negativos en la biodiversidad y la salud humana."

Groundwater_Contamination = "Se refiere a la contaminación de las aguas subterráneas, que son una fuente importante de agua potable. Sustancias químicas, contaminantes industriales o agrícolas pueden infiltrarse en el suelo y llegar a las aguas subterráneas, afectando la calidad del agua."

Electromagnetic_Pollution = "Se refiere a la exposición excesiva a campos electromagnéticos producidos por dispositivos electrónicos, antenas de telecomunicaciones y otros equipos. Aunque la investigación sobre sus efectos está en curso, se ha planteado preocupación sobre los posibles impactos en la salud humana."

Chemical_Spills = "Se refiere a la liberación accidental o intencionada de sustancias químicas peligrosas en el medio ambiente, como derrames de productos químicos tóxicos en tierra, agua o aire. Estos derrames pueden causar daño inmediato a la salud, la vida silvestre y el entorno."

Airborne_Allergens = "Se refiere a partículas biológicas como polen, esporas de hongos y otros alérgenos que están presentes en el aire y pueden desencadenar reacciones alérgicas en las personas susceptibles."

Acid_Rain = "Se refiere a la precipitación de lluvia con un pH más bajo de lo normal debido a la emisión de dióxido de azufre y óxidos de nitrógeno en la atmósfera. La lluvia ácida puede dañar ecosistemas acuáticos, suelos, edificios y cultivos, y contribuir a la degradación del medio ambiente."

@client.command()
async def contamination(ctx, type = "GENERAL"):
    if type.upper() == "GENERAL":
        await ctx.send(general)
    if type.upper() == "AIRE":
        await ctx.send(air_polution)
    if type.upper() == "AGUA":
        await ctx.send(water_contamination)
    if type.upper() == "SUELO":
        await ctx.send(soil_contamination)
    if type.upper() == "SONIDO":
        await ctx.send(sound_contamination)
    if type.upper() == "LUZ":
        await ctx.send(light_contamination)
    if type.upper() == "TERMICO":
        await ctx.send(Thermal_Pollution)
    if type.upper() == "RADIOACTIVO":
        await ctx.send(Radioactive_Contamination)
    if type.upper() == "PLASTICO":
        await ctx.send(Plastic_Pollution)
    if type.upper() == "RESIDUOS":
        await ctx.send(Hazardous_Waste_Pollution)
    if type.upper() == "BIOLOGICO":
        await ctx.send(Biological_Contamination)
    if type.upper() == "AGUA_DEL_SUELO":
        await ctx.send(Groundwater_Contamination)
    if type.upper() == "ELECTROMAGNETICO":
        await ctx.send(Electromagnetic_Pollution)
    if type.upper() == "QUIMICO":
        await ctx.send(Chemical_Spills)
    if type.upper() == "ALERGENOS":
        await ctx.send(Airborne_Allergens)
    if type.upper() == "LLUVIA_ACIDA":
        await ctx.send(Acid_Rain)
    
    

# Setting the command description for the 'server_info' command
server_info.description = "This command displays detailed information about the server."

# Setting the command brief for the 'server_info' command (a shorter description for use in the default help command)
server_info.brief = "Displays server information."

# Setting the command description for the 'Ideas' command
Ideas.description = "This command gives you an idea para luchar contra la contaminación."

# Setting the command brief for the 'Ideas' command (a shorter description for use in the default help command)
Ideas.brief = "Gives an Idea."

# Setting the command description for the 'Bidon' command
Bidon.description = "This command te dice qué contiene cada bidón de reciclaje dependiendo de qué color escribes."

# Setting the command brief for the 'Bidon' command (a shorter description for use in the default help command)
Bidon.brief = "Dice que contiene cada bidón."

# Setting the command description for the 'challenge' command
challenge.description = "This command randomly chooses 1 challenge out of 30 challenges in total"

# Setting the command brief for the 'challenge' command (a shorter description for use in the default help command)
challenge.brief = "Gives you a challenge to do at home"

# Setting the command description for the 'contamination' command
contamination.description = "This command explains what contamination is and each type of contamination"

# Setting the command brief for the 'contamination' command (a shorter description for use in the default help command)

contamination.brief = "Explains contamination to you"


client.run("MTEyOTA5MjQ5NzIzMTA2OTI0NA.GGKX3P.anTdhj1nemvr9Na3RD26FueU_9iLcK4xGlogNQ")