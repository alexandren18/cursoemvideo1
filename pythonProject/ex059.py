n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
função = 0
while função != 5:
    função = 0
    print("="*10,"Menu", "=" * 10)
    print('''    [1] para SOMAR
    [2] para MUTIPLICAR
    [3] para MAIOR
    [4] para NOVOS NUMEROS
    [5] para SAIR DO PROGRAMA''')
    função = int(input("Qual função você quer: "))
    if função == 2:
        print(f"A mutilplicação de {n1} x {n2} é igual a {n1*n2}")
    elif função == 1:
        print(f"A soma de {n1} + {n2} é igual a {n1+n2}")
    elif função == 3:
        if n1 > n2:
            print(f"{n1} é maior que {n2}")
        elif n2 > n1:
            print(f"{n2} é maior que {n1} ")
        else:
            print("os numeros são iguais")
    elif função == 4:
        n1 = int(input("Digite o primeiro numero: "))
        n2 = int(input("Digite o segundo numero: "))
    elif função != 1 and função != 2 and função != 3 and função != 4 and função != 5:
        print(" numero invalido, tente outro")
    else:
        print("Fim dsa operações")


    