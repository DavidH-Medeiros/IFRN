soma = 0
x = 2

while x < 2000000:
    divisor = 2
    primo = True

    while divisor * divisor <= x:
        if x % divisor == 0:
            primo = False
            break

        divisor = divisor + 1

    if primo:
        soma = soma + x

    x = x + 1

print(soma)