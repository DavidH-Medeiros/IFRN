soma = 0
quantidade = 0
menor = None

while True:
    numero = int(input("Digite um número inteiro (0 para encerrar): "))

    if numero == 0:
        break

    soma += numero
    quantidade += 1

    if menor is None or numero < menor:
        menor = numero

if quantidade > 0:
    media = soma / quantidade

    print("Menor valor digitado:", menor)
    print("Média dos valores digitados:", round(media, 2))
else:
    print("Nenhum valor válido foi digitado.")
