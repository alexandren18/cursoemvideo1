lista = []
while True:
    lista.append((input("Digite um numero: ")))
    continuar = str(input("Digite [S] para continuar e [N] para parar: ")).strip().upper()
    if continuar == "N":
        break
    elif continuar != 'S' and  continuar != "N":
        continuar = str(input("Acão invalida! Digite [S] para continuar ou [N] para sair: "))
print("-=" * 40)
print(f"Você digitou {len(lista)} numeros")
lista.sort(reverse=True)
print(f"OS valores em ordem reversa que foi digitado são {lista}")
if 5 in lista:
    print("Valor 5 faz parte da lista")
else:
    print("O valor 5 não faz parte da lista")