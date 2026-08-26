print ("coloque os valores de: A, B e C para que seja realizado a uma equação de segundo grau")
a = float(input("A:"))
b = float(input("B:"))
c = float(input("C:"))

delta = b**2-4*a*c

x1 = (-b + delta**0.5)/(2*a)
x2 = (-b - delta**0.5)/(2*a)

print ("Os valor de x1 é:", x1," e x2 é ", x2)