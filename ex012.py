produto = float(input("Digite o valor do produto: "))
desconto = produto - (produto*5/100)

print("O produto que custava {:.2f} com o desconto de 5% fica {:.2f}".format(produto,desconto))