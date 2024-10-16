somaidade = 0
maioridadehomem= 0
nomevelho = ""
totalmulher20 = 0
for i in range(1,5):
     print(f"-----{i}° PESSOA-----")
     nome = str(input("Qual seu nome: ")).strip()
     idade = int(input("Qual sua idade: "))
     sexo = str(input("Sexo [M/F]: "))
     somaidade += idade
     if i == 1 and sexo in "Mm":
          maioridadehomem = idade
          nomevelho = nome
     if sexo in "Mm" and idade > maioridadehomem:
          maioridadehomem = idade
          nomevelho = nome
     if sexo in "Ff" and idade < 20:
          totalmulher20 += 1
mediaidade = somaidade/4
print(f"A media de idade do grupo é de {mediaidade} anos")
print(f"O homem mais velho se chama {nomevelho} e tem {maioridadehomem} anos")
print(f"Ao todo são {totalmulher20} mulheres com menos de 20 anos")

