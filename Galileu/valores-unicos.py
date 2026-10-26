numeros = []

for i in range(10):
    valor = int(input("Digite um número inteiro: "))

    if valor not in numeros:
        numeros.append(valor)

numeros.sort()

print(numeros)
