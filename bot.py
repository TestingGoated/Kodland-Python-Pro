import discord
import random
import asyncio
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

@client.event
async def on_ready():
    print(f'Fizemos login como {client.user}')

@client.event
async def on_message(message):

    if message.author == client.user:
        return


    if message.content.startswith('!C.C'):
        fah = ["Coroa", "Cara"]
        resultado = random.choice(fah)  
        await message.channel.send("girando a moeda...")
        await message.channel.send(resultado)


    elif message.content.startswith('!senha'):
        senha = gen_pass(10)
        await message.channel.send(f"sua senha: {senha}")

   
    elif message.content.startswith('!guess'):
        await message.channel.send('Adivinhe um número entre 1 e 10 (você tem 5 segundos).')

        def is_correct(m):
            return m.author == message.author and m.channel == message.channel and m.content.isdigit()

        answer = random.randint(1, 10)

        try:
 
            guess = await client.wait_for('message', check=is_correct, timeout=5.0)
        except asyncio.TimeoutError:
            return await message.channel.send(f'Demorou muito! O número era {answer}.')

        if int(guess.content) == answer:
            await message.channel.send('Você acertou!')
        else:
            await message.channel.send(f'Errou! Na verdade era {answer}.')


    elif message.content.startswith("!lixo"):
            msg = message.content.lower()

            if "plastico" in msg:
                await message.channel.send("Lixeira VERMELHA!")
            elif "organico" in msg:
                await message.channel.send("Lixeira MARROM!")
            elif "metal" in msg:
                await message.channel.send("Lixeira AMARELA!")
            elif "papel" in msg:
                await message.channel.send("Lixeira AZUL!")
            elif "vidro" in msg:
                await message.channel.send("Lixeira VERDE!")
            else:
                await message.channel.send("Escreva o tipo junto! Exemplo: `!lixo vidro/plastico/metal/papel/organico`")


client.run('SEU TOKEN')
