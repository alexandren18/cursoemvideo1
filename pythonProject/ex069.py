p18 = 0
homem = 0
mulher = 0
while True:
    idade = int(input("Qual é sua idade : "))
    while True:
        sexo = str(input("[M/F]")).strip().upper()
        if sexo == "M" or sexo == "F":
            break
        else:
             print("Entrada invalida! Por favor, digite M  para masculino ou F para feminino")
    if idade > 18:
            p18 += 1
    if sexo == "M":
            homem += 1
    elif sexo == "F" and idade < 20:
        mulher += 1    
    while True:
        continuar = str(input("Quer continuar ? [S/N]")).strip().upper() 
        if continuar == "N" or continuar == "S":
            break
        else:
            print("Entrada invalida! Por favor, digite S para sim ou N para não.")
    if continuar == "N":
        break
print(f"Total de pessoas com mais de 18 anos: {p18}")
print(f"Ao todo temos {homem} homens cadastrados")
print(f"E temos {mulher} mulheres com menos de 20 anos")

        
