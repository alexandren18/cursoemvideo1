alunos = []

while True :
    nome = str(input("Digite o nome do aluno (ou 'sair' para finalizar): "))
    if nome.capitalize() == "Sair":
        break
    nota1 = float(input(f"DIgite primeira nota de {nome}: "))
    nota2 = float(input(f"Digite segunda nota de {nome}: "))
    media = (nota1 + nota2)/2
    alunos.append([nome,[nota1,nota2],media])

print("\nBoletim:")
print(f"{"No.":<4}{"Nome":<10}{"Média":>8}")
print("-" * 24)

for i,aluno in enumerate(alunos):
    print(f"{i:<4}{aluno[0]:<10}{aluno[2]:>8.2f}")


while True:
    opcao = int(input("\nMostrar notas de qual aluno? (999 para interromper): "))
    if opcao == 999:
         break
    if opcao < len(alunos):
         print(f"Notas de {alunos[opcao][0]} são {alunos[opcao][1]}")
    else: print("Aluno não encontrado.")
