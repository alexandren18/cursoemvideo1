v1 = int(input("Qual o primeiro valor ? "))
v2 = int(input("Qual o segundo valor ? "))
v3 = int(input("Qual o terceiro valor ? "))
menor = v1
maior = v1
if v2 < v1 and v2 < v3:
    menor = v2
if v3 < v2 and v3 < v1:
    menor = v3
if v2 > v1 and v2 > v3:
    maior = v2
if v3 > v1 and v3 > v2:
    maior =v3
print(f"O maior numero é {maior}, e o menor numero é {menor}")