valor = int(input("Digite o valor do saque: "))
valor_orig = valor
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

print("O valor original de ", valor_orig, "equivale a:")


if n100 > 0 :
    print("Cédula(s) de R$ 100,00:", n100)
if n50 > 0 :
    print("Cédula(s) de R$ 50,00:", n50)
if n20 > 0 :
    print("Cédula(s) de R$ 20,00:", n20)
if n10 > 0 :
    print("Cédula(s) de R$ 10,00:", n10)
if n5 > 0 :
    print("Cédula(s) de R$ 5,00:", n5)    
if n2 > 0 :
    print("Cédula(s) de R$ 2,00:", n2)
if moedas1 > 0 :
    print("Moeda(s) de R$ 1,00:", moedas1)
