n, k = map(int, input().split())
bino = [[0 for j in range(k+1)] for i in range(n+1)]

for i in range(n+1):
    bino[i][0] = 1
for i in range(k+1):
    bino[i][i] = 1

for i in range(1, n+1):
    for j in range(1, k+1):
        bino[i][j] = bino[i-1][j-1] + bino[i-1][j]

print(bino[n][k] % 10007)
