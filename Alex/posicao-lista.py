lista = [51, 14, 21, 53, 85, 21, 51]

n = int(input("digite um numero da lista"))

for i in range(len(lista)):
        if n == lista[i]:
                print("a posição é", i)
                break
    
