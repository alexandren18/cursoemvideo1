import random
a = input("digite o primeiro nome: ")
b = input("digite o segundo nome: ")
c = input("digite o terceiro nome: ")
d = input(" digite o quarto nome: ")
e = input("digite o quinto nome: ")
l = [a,b,c,d,e]
r = random.choice(l)
print(f"O aluno escolhido foi {r}")