nome = str(input("Digite seu nome completo: ")).strip()
print("Analisando seu nome...")
print(f"Seu nome com todas as letras maiusculas é {nome.upper()}")
print(f"Seu nome com todas as  letras minusculas é {nome.lower()}")
print(f"Seu nome seu nome tem {len(nome)-nome.count(" ")}")
print(f"Seu primeiro nome tem {nome.find(" ")} letras")
