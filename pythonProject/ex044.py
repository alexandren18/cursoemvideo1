print("{:=^40}".format(" LOJA NOGUEIRA "))
preço = float(input("Proço da compra: R$"))
print("Formas de pagamento")
print("[1] à vista dinheiro/cheque\n[2] à vista cartão\n[3] 2x no cartão\n[4] 3 ou mais vezes no cartão")
pagamento = int(input("Qual a forma de pagamento: "))
if pagamento == 1:
    desconto = preço * 10/100
    valor = preço - desconto
    print(f"A compra de {preço:.2f} com desconto de 10% fica {valor:.2f}")
elif pagamento == 2:
    desconto = preço * 5/100
    valor = preço - desconto
    print(f"A compra de {preço:.2f} com desconto de 5% fica {valor:.2f}")
elif pagamento == 3:
    print(f"A compra ficou {preço:.2f} sem desconto")
elif pagamento == 4:
    parcela = int(input("Quantas parcelas:"))
    juros = preço * 20/100
    valor = preço + juros
    total = valor / parcela
    print(f'Sua compra sera parcelada em {parcela} de {total:.2f}')
    print(f"A compra de {preço:.2f} com o juros fica {valor:.2f}")
else:
    print("Opção invalida de pagamento, tente novamente.")