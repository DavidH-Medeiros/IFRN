a = 1
while a <= 1000:
    b = a + 1
    while b <= 1000:
        c = 1000 - a - b
        if c > b and a*a + b*b == c*c:
            print(a, b, c)
        b += 1
    a += 1


for a2 in range(1, 1000):
    for b2 in range(a2 + 1, 1000):
        c2 = 1000 - a2 - b2
        if a2*a2 + b2*b2 == c2*c2:
            print(a2, b2, c2)