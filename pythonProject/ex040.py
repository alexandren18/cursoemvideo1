n1 = float(input("Digite sua primeira nota:"))
n2 = float(input("Digite sua segunda nota:"))
media = (n1 + n2)/2
if media < 5:
    print(f"Sua média foi {media:.1f}")
    print("Você foi REPROVADO!")
elif media >= 7:
    print({f"Sua média foi {media:.1f}"})
    print("Você foi aprovado, PARABÉNS!")
else:
    print(f"Sua média foi {media:.1f}")
    print("Você esta de RECUPERAÇÃO!")