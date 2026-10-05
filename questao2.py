largura = float(input("Digite a largura do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))
comprimento = float(input("Digite o comprimento do retângulo: "))

rendimento_tinta = float(input("Digite o rendimento da tinta (em m²/litro): "))

parede1 = largura * altura
parede2 = comprimento * altura
area_total = 2 * (parede1 + parede2)
quanto_tinta = area_total / rendimento_tinta * 2 #2 significa a quantidade de demãos

print("A área total das paredes é:", area_total, "m²")
print("A quantidade de tinta necessária para pintar as paredes é:", quanto_tinta, "litros")
