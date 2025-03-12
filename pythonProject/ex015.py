km = float(input("Quantos km rodados ? "))
dia = float(input("Quantos dias alugado ? "))
alu = (dia * 60) + (km * 0.15)
print("Valor a pagar do aluguel é {}".format(alu))