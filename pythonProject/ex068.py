from random import randint
contador = 0
while True:
    print("=-" * 15)
    print("VAMOS JOGAR PAR OU ÍMPAR")
    print("=-" * 15)
    computador = randint(1,10)
    n = int(input("Digite um valor: "))
    contador += 1
    resultado = str(input("Par ou Ímpar? [P/I] ")).strip().upper()
    print(f"você jogou {n} e o computador {computador}")
    if resultado == "P" and total % 2 != 0:
        print(f"Você jogou {n} e o computador {computador}")
        break
    if resultado == "I" and total % 2 == 0:
        print(f"Você jogou {n} e o computador {computador}")
        break

print("GAME OVER")

