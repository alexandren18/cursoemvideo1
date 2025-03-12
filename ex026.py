frase = str(input("Digite uma frase: ")).upper().strip()
print(f"A letra A aparece {frase.count("A")} vez")
print(f"A primeira letra A apareceu na prosição {(frase.find("A")+1)}")
print(f"a ultima letra A apareceu na posição {(frase.rfind("A")+1)}")