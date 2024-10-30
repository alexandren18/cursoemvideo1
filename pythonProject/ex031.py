viagem =float(input("Digite a distancia da viagem em km: "))
print(f"você ta preste a fazer uma viagem de {viagem} km/h")
if viagem<= 200:
    passagem = viagem * 0.50
else:
    passagem = viagem * 0.45
print(f"O valor da sua passagem é de {passagem} R$")
