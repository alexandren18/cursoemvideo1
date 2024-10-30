valortotal = 0
produto1000 = 0
menor = " "
barato = float("inf")
while True:
    produto = str(input("Nome do produto: ")).strip()
    valor = float(input("Preço: R$"))
    valortotal += valor
    if valor > 1000:
        produto1000 += 1
    if valor < barato:
        menor = produto
        barato = valor
    while True:
        continuar = str(input("Quer continuar [S/N]")).strip().upper()
        if continuar == "N" or continuar == "S":
            break
        else:
            print("Entrada invalida! Por favor, digite S para sim ou N para não.")
    if continuar == "N":
        break
print(f"O total da compra foi de {valortotal:.2f}R$")
print(f"Tem {produto1000} que valem mais de R$ 1000.00")
print(f"o produto mais barato foi {menor} e o preço foi {barato:.2f}")
        


