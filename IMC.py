altura = float(input("Escreva sua altura em cm:")) / 100
peso =float(input("Escreva seu em kg:"))

IMC = peso / (altura * altura)
if IMC < 18.5:
    print("Você está abaixo do peso")

elif IMC <= 24.9:
    print("Você está com o peso normal")

elif IMC <= 29.9:
    print("Você está com sobrepeso")

elif IMC <= 34.9:
    print("Você está em obesidade grau I")

elif IMC <= 39.9:
    print("Você está em obesidade grau II")

else:
    print("Você está em obesidade grau III, procure ajuda imediatamente!!!")

print("Seu IMC é:", IMC) 