numero = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito",
          "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis",
          "dezessete", "dezoito", "dezenove", "vinte")

while True:
    # Loop para garantir que o número esteja no intervalo correto
    while True:
        n = int(input("Digite um número entre 0 e 20: "))
        if 0 <= n <= 20:
            break
        print("Número inválido. Tente novamente um número entre 0 e 20.")

    print(f"Você digitou o número {numero[n]}")

    continuar = str(input("Você quer continuar? [S/N] ")).strip().upper()
    if continuar not in ["S", "N"]:
        continuar = str(input("Ação inválida! Digite S para continuar ou N para sair: "))

    if continuar == "N":
        break

print("FIM DO PROGRAMA")



