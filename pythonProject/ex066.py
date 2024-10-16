contador = 0
soma = 0
while True:
    n = int(input("Digite um numero(999 para parar): "))
    if n == 999:
        break
    soma += n
    contador +=1
    
print(f"você digitou {contador} valores e a soma entre eles é de {soma}")
