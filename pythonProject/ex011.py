largura = float(input("digite a largura da parede: "))
altura = float(input("digite a altura da parede: "))
area = largura*altura
tinta = area/2
print("Sua parede tem dimensão de {}x{} e sua area é de {}".format(largura,altura,area))
print("Para pintar essa parede você vai precisar de {}L de tinta".format(tinta))