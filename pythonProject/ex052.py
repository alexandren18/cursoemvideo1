n = int(input("Digite um numero:"))
primo = 0
for i in range(1,n+1):
    if n % i == 0:
        print("\033[33m", end=" ")
        primo+=1
    else:
        print("\33[31m", end=" ")
    print(f"{i}", end= " ")
print(f"\n\033[mO numero {n} foi divisivel {primo}")
if primo == 2:
    print("E por isso ele é primo")
else:
    print("E por isso ele não é primo")