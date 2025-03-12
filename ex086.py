coluna = [[],[],[]]
for c in range(0,9):
    if len(coluna[0]) < 3:
        coluna[0].append(int(input("Digite um valor: ")))
    elif len(coluna[1]) < 3:
        coluna[1].append(int(input("Digite um valor: ")))
    elif len(coluna[2]) < 3:
        coluna[2].append(int(input("Digite um valor: ")))

print(coluna[0])
print(coluna[1])
print(coluna[2])

