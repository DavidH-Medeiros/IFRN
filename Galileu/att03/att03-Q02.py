
dp = [[0] * 10 for _ in range(10)]

for a in range(1, 10):
    for b in range(10):
        dp[a][b] = 1

for tamanho in range(3, 10):

    novo_dp = [[0] * 10 for _ in range(10)]

    for a in range(10):
        for b in range(10):

            if dp[a][b] > 0:

                for c in range(10):

                    if a + b + c <= 8:

                        novo_dp[b][c] += dp[a][b]

    dp = novo_dp

total = 0

for a in range(10):
    for b in range(10):
        total += dp[a][b]

print("Quantidade de números válidos:", total)
