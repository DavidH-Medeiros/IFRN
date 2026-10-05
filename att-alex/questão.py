n1 = int(input("Digite a nota do 1º bimestre: "))
n2 = int(input("Digite a nota do 2º bimestre: "))
n3 = int(input("Digite a nota do 3º bimestre: "))
n4 = int(input("Digite a nota do 4º bimestre: "))

media = (n1 + n2 + n3 + n4) / 4
print("A média das notas é:", int(media))
if media >= 70:
    print("Aprovado")
elif media >= 40:
    print("Recuperação")
    notarecuperacao = 140 - media
    print("Nota necessária para passar na recuperação:", int(notarecuperacao))
else:
    print("Reprovado")