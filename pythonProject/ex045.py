from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0,2)
print('''Suas opções
[0] Pedra
[1] Papel
[2] Tesoura''')
voce = int(input("Qual é sua jogada: "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
print("-="*11)
print(f"Computador jogou {itens[computador]}")
print(f"Jogador jogou {itens[voce]}")
if computador == 0:
    if voce == 0:
        print("Empatou")
    elif voce == 1:
        print("Você ganhou")
    elif voce == 2:
        print("O computador ganhou")
elif computador == 1:
    if voce == 0:
        print("O computador ganhou")
    elif voce == 1:
        print("Empatou")
    elif voce == 2:
        print("Você ganhou")
elif computador == 2:
    if voce == 0:
        print("você ganhou")
    elif voce == 1:
        print("O computador ganhou")
    elif voce == 2:
        print("Empatou")


