from datetime import date
m = 0
n = 0
atual = date.today().year
for i in range(1,8):
    n1 = int(input(f"Em que ano a {i}° pessoa nasceu: "))
    if atual - n1 >= 21:
        m += 1
    elif atual - n1 < 21:
        n += 1
print(f"tem {m} pessoas maior de idade e {n} são menores de idade")