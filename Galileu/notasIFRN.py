N1 = float(input("Digite a nota N1: "))
N2 = float(input("Digite a nota N2: "))

MD = (2 * N1 + 3 * N2) / 5

print("Média (MD):", MD)

if MD >= 60:
    print("APROVADO POR MÉDIA")

elif MD >= 20:
    print("Não aprovado por média.")
    print("O aluno tem direito à prova final.")

    NAF = float(input("Digite a nota da avaliação final (NAF): "))

    MFD1 = (MD + NAF) / 2
    MFD2 = (2 * NAF + 3 * N2) / 5
    MFD3 = (2 * N1 + 3 * NAF) / 5

    MFD = max(MFD1, MFD2, MFD3)

    print("MFD 1: ", MFD1)
    print("MFD 2: ", MFD2)
    print("MFD 3: ", MFD3)
    print("Maior MFD: ", MFD)

    if MFD >= 60:
        print("APROVADO POR PROVA FINAL")
    else:
        print("REPROVADO")

else:
    print("REPROVADO")