lista = []
for c in range(0,5):
    valor = int(input("Digite um numero: "))
    if c == 0 or valor > lista[-1]:
        lista.append(valor)
    else:
        pos = 0
        while pos < len(lista):
            if valor <= lista[pos]:
                lista.insert(pos,valor)
                break
            pos += 1
print("-=" * 30)
print(f"Os valores digitado em ordem foram {lista}")

