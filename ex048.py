soma = 0
contador = 0
for i in range (1,501,2):
    if i % 3 == 0:
        soma += i
        contador += 1
print(f"A soma de todos {contador} é de {soma}")
