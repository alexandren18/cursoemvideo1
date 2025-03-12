casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o seu salario: "))
anos = float(input("Em quantos anos você vai pagar ? "))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print(f"Para pagar uma casa de {casa:.2f} em {anos},a prestação sera de {prestacao:.2f}")
if prestacao <= minimo:
    print("Empréstimo pode ser concedido.")
else:
    print("Empréstimo negado!")

