a = 1

while a <= 1000:
    b = a + 1
    while b <= 1000:
        c = 1000 - a - b
        if a*a + b*b == c*c:
            print(a, b, c)
        b += 1
    a += 1