from datetime import date
ano = int(input("Qual ano quer analisar ? Digite 0 para o ano atual: "))
if ano == 0:
    ano = date.today().year
if ano % 2 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print(f"{ano} é um ano bissexto")
else:
    print(f"{ano} não é um ano bissexto")