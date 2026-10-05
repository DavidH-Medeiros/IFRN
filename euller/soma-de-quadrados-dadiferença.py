soma1 = 0
x = 1
while x <= 10:
    soma1 = soma1 + x ** 2
    x += 1
print(soma1)

soma2 = 0
y = 1
while y <= 10:
    soma2 = soma2 + y
    y += 1
soma2 = soma2 ** 2
print(soma2)

print("A diferença entre as somas é:", soma2 - soma1)