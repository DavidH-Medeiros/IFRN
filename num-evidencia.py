x = int(input("Digite um numero: "))
e = x

while x > 1:
    e = e * (x - 1)
    x = x - 1

print("em evidencia é:", e)