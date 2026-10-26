lista = [5, 10, 12,21]
lista2 = []

for i in range(len(lista)-1):
    lista2.append(lista[i]+lista[i+1])

print(lista2)