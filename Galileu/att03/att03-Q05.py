n = int(input("Digite um número entre 100 e 9999: "))

ultimo = n % 10

resto = n // 10

if n >= 1000:
    resultado = ultimo * 1000 + resto
elif n >= 100:
    resultado = ultimo * 100 + resto

print("Número rotacionado:", resultado)
