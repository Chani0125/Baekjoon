import sys

n = int(sys.stdin.readline())
m = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]

for t in range(1, n):
    for i in range(n-t):
        dp[i][i+t] = dp[i][i] + dp[i+1][i+t] + m[i][0] * m[i][1] * m[i+t][1]
        for j in range(1, t):
            dp[i][i+t] = min(dp[i][i+t], dp[i][i+j] + dp[i+j+1][i+t] + m[i][0] * m[i+j][1] * m[i+t][1])

# for i in dp:
#     for j in i:
#         print(j, end=" ")
#     print()

print(dp[0][n-1])