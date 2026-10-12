numeros = []

while True:
    entrada = input("Digite um número ou FIM para encerrar: ")

    if entrada.upper() == "FIM":
        break

    numeros.append(float(entrada))

triplo = [numero * 3 for numero in numeros]

print("Lista original:", numeros)
print("Triplo dos valores:", triplo)