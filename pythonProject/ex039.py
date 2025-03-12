from datetime import date
ano = int(input("Digite o ano que você nasceu:"))
atual = date.today().year
idade= atual - ano
print(f" quem nasceu em {ano} tem {idade} em {atual}")
if idade < 18:
    saldo = 18 - idade
    print(f" você tem {idade} anos, ainda vai se alistar")
    print(f"Você tem que se alistar em {atual + saldo}")
elif idade == 18:
    print(f"Você tem {idade} anos, hora de se alistar")
else:
    saldo = idade - 18
    print(f"Você tem {idade} anos, passou da hora de se alistar ")
    print(f"Você tinha que se alistar em {atual - saldo}")