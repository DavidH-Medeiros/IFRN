numero = int(input("Digite um número inteiro positivo: "))

original = numero

quantidade_digitos = 0
temp = numero

while temp > 0:
    quantidade_digitos += 1
    temp = temp // 10

soma = 0
temp = numero

while temp > 0:
    digito = temp % 10

    potencia = digito ** quantidade_digitos

    soma += potencia

    temp = temp // 10

if soma == original:
    print(original, "é um número de Armstrong.")
else:
    print(original, "não é um número de Armstrong.")
