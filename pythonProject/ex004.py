n = input("Digite algo : ")
print("O tipo primitivo desse valor é : ",type(n))
print("Só tem espaço? ", n.isspace())
print("É um numero ? ", n.isnumeric())
print("É alfabético ? ", n.isalpha())
print("É alfanumérico ? ", n.isalnum())
print("Esta em maiusculas ? ", n.isupper())
print("Esta em minusculas ? ", n.islower())
print("Esta capitalizada ? ", n.istitle())