n1 = (int(input("Digite um numero: ")),int(input("Digite um numero: "))
      ,int(input("Digite um numero: ")),int(input("Digite um numero: ")),)
print(f"Você digitou os valores {n1}")
print(f"O valor 9 apareceu {n1.count(9)} vezes.")
if n1 == 3:
    print(f"O valor 3 apareceu na {n1.index(3)+1}° posição ")
else:
    print("O valor 3 não foi digitado em nenhuma posição")
print(f" os numeros  pares digitados foram", end=" ")
for n in n1:
    if n % 2 == 0:
        print(n,end= ", ")
