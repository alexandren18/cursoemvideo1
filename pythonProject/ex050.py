soma = 0
contador = 0
for i in range(0,6):
    n = int(input("Digite um numero: "))
    if n % 2 == 0:
        soma+=n
        contador+= 1
print(f"Você informou {contador} numeros pares e a soma deles é {soma}")
