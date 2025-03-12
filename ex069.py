p18 = 0
homem = 0
mulher20 = 0
while True:
    print("-" * 30)
    print("CADASTRE UMA PESSOA")
    print("-" * 30)
    idade = int(input("Idade: "))
    while True:
        sexo = str(input("Sexo: [M/F]")).strip().upper()
        if sexo == "M" or sexo == "F":
            break
    if idade > 18 :
        p18 += 1
    if sexo == "M":
        homem += 1
    if idade < 20 and sexo == "F":
        mulher20 += 1
    while True:
        continuar = str(input("quer continuar: [S/N]")).strip().upper()
        if continuar == "S" or continuar == "N":
            break
    if continuar == "N":
        break
print(f"Total de pessoas com mais de 18 anos: {p18}")
print(f"Ao todo temos {homem} homens cadastrados.")
print(f"E temos {mulher20}  mulheres com menos de 20 anos.")
        
        



        
