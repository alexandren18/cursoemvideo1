from random import randint
vitoria = 0
while True:
    print("=-" * 15)
    print("VAMOS JOGAR PAR OU ÍMPAR")
    print("=-" * 15)
    computador = randint(1,10)
    jogador = int(input("Digite um valor: "))
    total = computador + jogador
    parouimpar = " "
    while True:
        parouimpar = str(input("Digite [P] para par ou [I] para impar: ")).strip().upper()
        if parouimpar == "P" or parouimpar == "I":
            break
        
    if parouimpar == "P" and total % 2 != 0:
        print(f"Você colocou {jogador} e o computador {computador}. Total de {total} deu ímpar")
        print("Você perdeu!")
        break
    if parouimpar == "I" and total % 2 == 0:
        print(f"Você colocou {jogador} e o computador {computador}. Total de {total} deu par")
        print("Você perdeu")
        break
    if parouimpar == "P" and total % 2 == 0:
        print(f"Você colocou {jogador} e o computador {computador}. Total de {total} deu par")
    elif parouimpar == "I" and total % 2 != 0:
        print(f"Você colocou {jogador} e o computador {computador}. Total de {total} deu ímpar")
    vitoria += 1
    print("Você venceu!")
    print("Vamos jogar novamente...")

print("Game over!")
print(f"você ganhou {vitoria} seguidas")
