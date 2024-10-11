import random
a = str(input("Digite o primeiro nome: "))
b = str(input("Digite o segundo nome: "))
c = str(input("Digite o terceiro nome: "))
d = str(input("Digite o quarto nome: "))
e = str(input("Digite o quinto nome: "))
l = [a,b,c,d,e]
random.shuffle(l)
print(f"a ordem da apresentação é {l}\n l")