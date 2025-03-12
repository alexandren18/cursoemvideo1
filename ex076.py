produtos_organizados = (
    "Açúcar", 3.50, "Arroz", 20.99, "Azeite", 15.29, "Café", 10.99, 
    "Feijão", 8.49, "Farinha", 4.99, "Leite", 3.89, "Macarrão", 4.79, 
    "Óleo", 6.49, "Sal", 2.20
)
print("-"*40)
print(f"{"LISTAGEM DE PREÇO":^40}")
for c in range(0,len(produtos_organizados)):
    if c % 2 == 0:
        print(f"{produtos_organizados[c]:.<30}",end="")
    else:
        print(f"R$  {produtos_organizados[c]:.2f}")
print("-"*40)





