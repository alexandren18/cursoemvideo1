lista = [[], []]
for p in range(0,7):
    valor = int(input("Digite um valor: "))
    if valor % 2 == 0:
        lista[1].append(valor)
    else:
        lista[0].append(valor)

print("-="*15)
lista[0].sort()
lista[1].sort()
print(f"Os valores pares {lista[1]}")
print(f"Os valores impares foram {lista[1]}")