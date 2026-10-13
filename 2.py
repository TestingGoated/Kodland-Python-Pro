import random

limit = "1234567890"

password = int(input("digite o numero de digitos que sua senha devera ter: "))

senha = ""

for i in range(password):
    aleatorio = random.choice(limit)
    senha += aleatorio

print(senha)

