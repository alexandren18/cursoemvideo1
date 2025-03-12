pessoas = []
dados = []
maior = menor = 0


while True:
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if maior < dados[1]:
            maior = dados[1]
        if menor > dados[1]:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    continuar = str(input("Deseja continuar [S] para sim e [N] para não ?")).upper().strip()
    if continuar != "S" and continuar != "N":
        continuar = str(input("Invalido, tenta novamente! [S] para sim e [N] para não ?"))
    if continuar == "N":
        break


print(f"-="*30)
print(f"Os dados são {pessoas}")
print(f"{len(pessoas)} pessoas foram cadastradas")
print(f"O maior peso foi de {maior:.2f}KG.Peso de",end=" ")
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}', end=" ")
print()
print(f"O menor peso  foi de {menor:.2f}KG.Peso de",end=" ")
for p in pessoas:
    if p[1] == menor:
        print(f"{p[0]}",end=" ")
print()




