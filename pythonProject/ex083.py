# Solicita ao usuário para digitar uma expressão
expr = str(input('Digite a expressão: '))

# Cria uma lista para funcionar como pilha
pilha = []

# Itera sobre cada símbolo na expressão
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

# Verifica se a pilha está vazia (expressão válida) ou não (expressão inválida)
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
