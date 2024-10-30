lista = []
maior = 0
menor = 0
for c in range(0,5):
    lista.append(int(input(f"Digite um valor para posição {c}: ")))
    if c == 0:
        maior = menor = lista[c]
    else:
        if maior < lista[c]:
            maior = lista[c]
        if menor > lista[c]:
            menor = lista[c]
print("-="*30)
print(f"Você digitou os valores {lista}")
print(f" o maior valor foi {maior} na posição",end=" ")
for i,v in enumerate(lista):
    if v == maior:
        print(f"{i}...",end=" ")
print()
print(f"O menor valor foi {menor} na posição",end=" ")
for i,v in enumerate(lista):
    if v == menor:
        print(f"{i}...",end=" ")
print()