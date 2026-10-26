
valor_mensal = float(input("Informe o valor mensal a ser aplicado (R$): "))
taxa = float(input("Informe a taxa de juros mensal (%): "))

saldo = 0
ano = 1

while True:
    for mes in range(12):
        saldo = saldo + valor_mensal
        saldo = saldo + (saldo * taxa / 100)

    print(f"O valor acumulado do {ano}º ano é (R$): {saldo:.2f}")

    resposta = input("Deseja calcular mais um ano (S/N)? ").upper()

    if resposta != "S":
        break

    ano += 1
