import discord
import random
import asyncio

# Configuração das intenções do bot
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
    # Ignorar mensagens do próprio bot para evitar loops
    if message.author == client.user:
        return

    # 1. Comando para girar a moeda
    if message.content.startswith('!C.C'):
        fah = ["Coroa", "Cara"]
        resultado = random.choice(fah)
        await message.channel.send("girando a moeda...")
        await message.channel.send(resultado)

    # 2. Comando para gerar senha
    elif message.content.startswith('!senha'):
        senha = gen_pass(10)
        await message.channel.send(f"sua senha: {senha}")

    # 3. Jogo de Adivinhação (Guess)
    elif message.content.startswith('!guess'):
        await message.channel.send('Adivinhe um número entre 1 e 10 (você tem 5 segundos).')

        def is_correct(m):
            return m.author == message.author and m.channel == message.channel and m.content.isdigit()

        answer = random.randint(1, 10)

        try:
            # Aguarda a resposta do mesmo usuário no mesmo canal
            guess = await client.wait_for('message', check=is_correct, timeout=5.0)
        except asyncio.TimeoutError:
            return await message.channel.send(f'Demorou muito! O número era {answer}.')

        if int(guess.content) == answer:
            await message.channel.send('Você acertou!')
        else:
            await message.channel.send(f'Errou! Na verdade era {answer}.')

client.run('token')
