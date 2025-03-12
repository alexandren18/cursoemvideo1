import time 
import random 
print("-"*40)
print(f"           JOGA NA MEGA SENA ")
print("-"*40)

# Pergunta quantos jogos o usuário deseja gerar
num_jogos = int(input("Quantos jogos você quer gerar? "))

palpites = []
for _ in range(num_jogos):
    jogo = random.sample(range(1, 61), 6)
    palpites.append(sorted(jogo))

# Exibe os palpites gerados com uma pausa de 1 segundo entre cada um
print("\nPalpites Gerados:")
for i, palpite in enumerate(palpites, start=1):
    print(f"Jogo {i}: {palpite}")
    time.sleep(1)



