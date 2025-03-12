lista = []
while True:
    valor = int(input("Digite um valor: "))
    if valor in lista:
        print("Valor duplicado, não vou adicionar.")
    else:
        lista.append(valor)
        print("Valor adicionado com sucesso")
    continuar = str(input("Digite [S] para continuar e [N] para sair: ")).strip().upper()
    if continuar == "N":
        break
    while True:
        if continuar != "N" and continuar != "S":
            continuar = str(input("Invalido tente novamente: ")).strip().upper()
        else:
            break
lista.sort()
print("-=" * 40)
print(f"Os valores digitados {lista}")

    