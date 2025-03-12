from unicodedata import decimal

numero = int(input("Digite um numero inteiro:"))
print('''Escolha uma das bases para conversão
[1] para BINARIO
[2] para OCTAL
[3] para HEXADECIMAL''')
opção = int(input("Sua opção:"))
if opção == 1:
    print(f"{numero} convertido para binario é {bin(numero)[2:]}")
elif opção == 2:
    print(f"{numero} convertido para decimal é {oct(numero)[2:]}")
elif opção == 3:
    print(f"{numero} convertido para hexadecimal é {hex(numero)[2:]}")
else:
    print("Opcão invalida!")

