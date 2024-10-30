import math
a = float(input("Digite o angulo que você deseja: "))
s = math.sin(math.radians(a))
print(f"O angulo de {a:.2f} tem o seno de {s:.2f}")
c = math.cos(math.radians(a))
print(f"O  angulo de {a:.2f} tem o cosseno de {c:.2f}")
t = math.tan(math.radians(a))
print(f"O angulo de {a:.2f} tem a tangente de {t:.2f}")