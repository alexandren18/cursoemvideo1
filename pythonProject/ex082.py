lista = []
par = []
impar = []
while True:
    valor = int(input("Digite um valor: "))
    lista.append(valor)
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
    continuar = str(input("Quer continuar? Digite [S] Para sim ou [N] para não: ")).strip().upper()
    if continuar == "N":
        break
    while True:
        if continuar != "S" and "N":
            continuar = str(input("Invalido! Digite [S] para contiinuar ou [N] para sair: ")).strip().upper()
        else:
            break
print(f"A lista completa é {lista}")
print(f"A lista dos numeros pares é {par}")
print(F"A lista dos numeros impares é {impar}")