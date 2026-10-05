a1 = int(input("Digite o primeiro numero: "))
a2 = int(input("Digite o segundo numero: "))
b1 = int(input("Digite o terceiro numero: "))
b2 = int(input("Digite o quarto numero: "))

if a1 <= b1 and a2 > b1:
    print("As linhas se tocam")
elif b1 <= a1 and b2 > a1:
    print("As linhas se tocam")
else:
    print("As linhas não se tocam")



