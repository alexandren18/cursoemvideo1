from random import randint
import time
print(f"Vou pensar em um numero de 1 a 5. Tente adivinhar...")
computador = randint(1,5)
jogador = int(input(f"Em que numero eu pensei? "))
print("Processando...")
time.sleep(3)
if n1 == computador:
    print(f"Parabéns você acertou o numero era {computador}")
else:
    print(f"Você errou o numero era {computador}")
