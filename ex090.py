escola = {}
escola["nome"] = str(input("Digite nome: "))
escola["média"] = float(input(f"Média de {escola["nome"]}: "))

if escola["média"] > 7:
    escola["situação"] = "aprovado"
elif 5 <= escola["média"] < 7:
    escola["situação"] = "recuperação"
else:
    escola["situação"] = "reprovado"

print("-=" * 30)
for k, v in escola.items():
    print(f" - {k} é igual a {v}")


