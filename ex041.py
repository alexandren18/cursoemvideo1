idade = int(input("Digite sua idade: "))
if idade < 9:
    print("Sua categoria é mirim")
elif idade <= 14:
    print("Sua categoria é infantil")
elif idade <= 19:
    print("Sua categoria é Junior")
elif idade >=25:
    print("Sua categoria é Senior")
else:
    print("Sua categoria é master")