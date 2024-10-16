contador = 0
soma = 0
n = 0
n = int(input("Digite um numeor (999 para parar): "))
while n != 999:
    contador +=1
    soma += n
    n = int(input("Digite um numeor (999 para parar): "))
print(f"você digitou {contador} numeros e a soma dos numeros é {soma}")
