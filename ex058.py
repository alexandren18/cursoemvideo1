contador = 1
from random import randint
from time import sleep
computador = randint(0,10)
jogador = int(input("Em que numero eu pensei: "))
if jogador == computador:
    print(f"Parabéns o numero era {computador} e você precisou de {contador}")
else:
    while jogador != computador:
        contador += 1
        print(f"você errou o numero era {computador}")
        print("tente de novo")
        computador = randint(0,10)
        jogador = int(input("Em que numero eu pensei: "))
print(f"Parabéns você ganhou e você precisou de {contador} tentativas")
