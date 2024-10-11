print(30*"=")
print("   10 TERMOS DE UMA PA   ")
print(30*"=")
p = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão: "))
d = p + (10 -1) * r
for i in range(p,d+1,r):
    print(i,end=" ")
print("Acabou")