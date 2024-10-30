tabela = ("Botafogo", "Palmeiras", "Fortaleza", "Flamengo", "São Paulo"
          , "Internacional", "Bahia", "Cruzeiro", "Atlético-MG",
          "Vasco", "Grêmio", "Criciúma", "Red Bull Bragantino", "Juventude", "Athletico-PR", "Fluminense"
          , "Vitória", "Corinthians", "Cuiabá", "Atlético-GO")
print("-=" * 30)
print(f"os 5 primeiro colocados do Brasileirão são {tabela[0:5]}")
print("-=" * 30)
print(f"Os ultimos 4 colocados do Brasileirão são {tabela[-4:]}")
print("-=" * 30)
print(f"tabela em ordem alfabetica{sorted(tabela)}")
print("-=" * 30)
print(f"O fluminense ta na {tabela.index("Fluminense")+1}° posição")
