salario = float(input("Digite o salário mensal (R$): "))


if salario <= 2428.80:
    aliquota = 0
    parcela = 0
elif salario <= 2826.65:
    aliquota = 0.075
    parcela = 182.16
elif salario <= 3751.05:
    aliquota = 0.15
    parcela = 394.16
elif salario <= 4664.68:
    aliquota = 0.225
    parcela = 675.49
else:
    aliquota = 0.275
    parcela = 908.73

imposto = salario * aliquota - parcela


if imposto < 0:
    imposto = 0


if salario <= 5000:
    reducao = min(imposto, 312.89)
elif salario <= 7350:
    reducao = 978.62 - (0.133145 * salario)
    reducao = max(0, min(imposto, reducao))
else:
    reducao = 0

imposto_final = max(0, imposto - reducao)


salario_liquido = salario - imposto_final


print("\n--- Resultado ---")
print(f"Salário bruto: R$ {salario:.2f}")
print(f"Imposto antes da redução: R$ {imposto:.2f}")
print(f"Redução do imposto: R$ {reducao:.2f}")
print(f"Imposto de renda a pagar: R$ {imposto_final:.2f}")
print(f"Salário líquido: R$ {salario_liquido:.2f}")