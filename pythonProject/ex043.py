peso = float(input("Digite seu peso:"))
altura = float(input("Digite sua altura:"))
imc = peso / (altura ** 2)
print(f"O imc dessa pessoa é {imc:.1f}")
if imc < 18.5:
    print("Abaixo do peso.")
elif imc >= 18.5 and imc < 25:
    print("Peso ideal")
elif imc >= 25 and imc < 30:
    print("sobrepeso")
elif imc >= 30 and imc < 40:
    print("Obesidade")
else:
    print("obesidade morbida")