valor = int(input("Digite o valor do saque: "))

n100 = valor // 100
valor = valor % 100

n50 = valor // 50
valor = valor % 50

n20 = valor // 20
valor = valor % 20

n10 = valor // 10
valor = valor % 10

n5 = valor // 5
valor = valor % 5

n2 = valor // 2
valor = valor % 2

moedas1 = valor // 1

print("Cédulas de R$ 100,00:", n100)
print("Cédulas de R$ 50,00:", n50)
print("Cédulas de R$ 20,00:", n20)
print("Cédulas de R$ 10,00:", n10)
print("Cédulas de R$ 5,00:", n5)
print("Cédulas de R$ 2,00:", n2)
print("Moedas de R$ 1,00:", moedas1)