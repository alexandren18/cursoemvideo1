frase = "Alexandre Nogueira Araujo Lopes"

indice = 0
qtd_apareceu_mais_vezes_letra = 0
letra_apareceu_mais_vezes = ""

while indice < len(frase):
    letra_atual = frase[indice]
    qtd_apareceu_mais_vezes_letra_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes_letra < qtd_apareceu_mais_vezes_letra_atual:
        qtd_apareceu_mais_vezes_letra = qtd_apareceu_mais_vezes_letra_atual
        letra_apareceu_mais_vezes = letra_atual

    indice += 1

print(f'{qtd_apareceu_mais_vezes_letra}')
print(letra_apareceu_mais_vezes)
