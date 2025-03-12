numero = int(input("Digite o numero: "))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print("Analisando numero...")
print(f"O numero {numero} tem {u} unidade")
print(f"O numero {numero} tem {d} dezena")
print(f"O numero {numero} tem {c} centena ")
print(f"O numero {numero} tem {m} milhar")