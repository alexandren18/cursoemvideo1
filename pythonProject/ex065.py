contador = 0
soma = 0
continuar = " "
maior = 0
menor = 0
while continuar != "N":
    n1 = int(input("Digite um numero: "))
    contador += 1
    soma += n1
    continuar = str(input("digite S para continuar e N para encerrar: ")).upper()
    if contador == 1:
        maior = n1
        menor = n1
    else:
        if maior < n1:
            maior = n1
        if menor > n1:
            menor = n1
media = soma/contador
print(f" você digitou {contador} e a média foi {media:.2f}")
print(f" o menor numero foi {menor} e o maior numero foi {maior}")
