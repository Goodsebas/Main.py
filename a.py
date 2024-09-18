import discord
import random
import os
from bot2 import gen_pass
from discord.ext import commands
from duck import get_duck_image_url

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix = "$" ,intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')


@bot.command()
async def hello(ctx):
    await ctx.send("Hi!")

@bot.command()
async def bye(ctx):
    await ctx.send("😢")

@bot.command()
async def password(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.group()
async def cool(ctx):
    """Says if a user is cool.
    
    In reality, this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        if ctx.subcommand_passed:
            user = ctx.message.mentions[0] if ctx.message.mentions else None
            if user:
                await ctx.send(f'Yes, {user.display_name} is cool.')
            else:
                await ctx.send(f'No, I could not find the user you mentioned.')
        else:
            await ctx.send(f'No, {ctx.subcommand_passed} is not cool')

@bot.command()
async def mem_aleatorio(ctx):
    mem_alert = random.choice(os.listdir("image") )
    with open(f'image/{mem_alert}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def musica(ctx):
    '''Recomienda una música aleatoria'''
    canciones = [
        "Bohemian Rhapsody - Queen",
        "Billie Jean - Michael Jackson",
        "Chica Paranormal - Paulo Londra",
        "Goosebumps - Travis Scott",
        "Memorias - Mora-Jhayco",
        "Hey Jude - The Beatles",
        "Shape of You - Ed Sheeran",
        "Uptown Funk - Mark Ronson ft. Bruno Mars",
        "Blinding Lights - The Weeknd",
        "Rolling in the Deep - Adele"
    ]
    
    cancion = random.choice(canciones)
    await ctx.send(f'🎶 Te recomiendo escuchar: {cancion}')

@bot.command(name='bienvenida')
async def bienvenida(ctx):
    mensaje_bienvenida = """
    🎉 ¡Bienvenido/a al bot de reducción de residuos! ♻️

    Aquí tienes algunos comandos útiles para empezar a reducir tus residuos en casa:

    🔹 `$consejo` - Obtén un consejo sobre cómo reducir residuos.
    🔹 `$reciclar [material]` - Aprende a reciclar materiales específicos como plástico, vidrio o papel.
    🔹 `$receta` - Recibe una receta para aprovechar las sobras de comida.
    🔹 `$desafio` - Participa en un desafío semanal para reducir residuos.
    🔹 `$progreso [avance]` - Registra tu progreso en la reducción de residuos o consulta tus avances anteriores.

    🌱 ¡Estamos aquí para ayudarte a crear un hogar más sostenible! ¡No dudes en usar los comandos y empezar hoy! 🌍
    """
    await ctx.send(mensaje_bienvenida)

# Lista de consejos sobre cómo reducir residuos
consejos = [
    "Evita productos desechables y usa alternativas reutilizables.",
    "Compra a granel para reducir el uso de envases plásticos.",
    "Comienza a hacer compostaje en casa con residuos orgánicos.",
    "Usa envases de vidrio en lugar de plástico para almacenar alimentos.",
    "Lleva una bolsa reutilizable cada vez que vayas de compras."
]

# Comando para dar un consejo aleatorio
@bot.command(name='consejo')
async def consejo(ctx):
    consejo_aleatorio = random.choice(consejos)
    await ctx.send(f"♻️ Consejo para reducir residuos: {consejo_aleatorio}")

# Comando para mostrar una guía de reciclaje
@bot.command(name='reciclar')
async def reciclar(ctx, material=None):
    if material == "plastico":
        await ctx.send("Consejo: Asegúrate de lavar los envases de plástico antes de reciclarlos.")
    elif material == "vidrio":
        await ctx.send("Consejo: Reutiliza frascos de vidrio y si los reciclas, deposítalos en el contenedor verde.")
    elif material == "papel":
        await ctx.send("Consejo: Recicla papel limpio y seco en el contenedor azul.")
    else:
        await ctx.send("Por favor, especifica un material para reciclar: plastico, vidrio, papel.")

# Comando para sugerir una receta usando sobras
@bot.command(name='receta')
async def receta(ctx):
    recetas = [
        "Sopa de vegetales con restos de verduras.",
        "Tortilla de sobras: usa cualquier verdura o carne que tengas.",
        "Smoothie de frutas maduras que están por echarse a perder."
    ]
    receta_aleatoria = random.choice(recetas)
    await ctx.send(f"🍲 Receta para aprovechar sobras: {receta_aleatoria}")

# Comando para dar un desafío semanal
@bot.command(name='desafio')
async def desafio(ctx):
    desafios = [
        "Esta semana, intenta no comprar productos envueltos en plástico.",
        "Reduce el desperdicio de alimentos planificando tus comidas diarias.",
        "Reutiliza envases y frascos en lugar de comprar nuevos recipientes."
    ]
    desafio_aleatorio = random.choice(desafios)
    await ctx.send(f"🚀 Desafío de la semana: {desafio_aleatorio}")

# Comando para llevar un registro de progreso
progreso = {}

@bot.command(name='progreso')
async def registrar_progreso(ctx, avance: str = None):
    usuario = ctx.author.name
    if usuario not in progreso:
        progreso[usuario] = []

    if avance:
        progreso[usuario].append(avance)
        await ctx.send(f"¡Progreso registrado! {avance}")
    else:
        avances_usuario = progreso.get(usuario, [])
        if avances_usuario:
            avances_formateados = "\n".join(avances_usuario)
            await ctx.send(f"📊 Progreso de {usuario}:\n{avances_formateados}")
        else:
            await ctx.send("No has registrado ningún progreso todavía. ¡Empieza hoy!")
            
bot.run("")
