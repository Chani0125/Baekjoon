import sys

input = sys.stdin.readline
a = list(map(int, input().split()))
n = len(a)

INF = 1000000000
dp = [[[INF, ] * 5 for _ in range(5)] for _ in range(len(a))]
dp[0][0][0] = 0

mv = [
    [1, 2, 2, 2, 2],
    [0, 1, 3, 4, 3],
    [0, 3, 1, 3, 4],
    [0, 4, 3, 1, 3],
    [0, 3, 4, 3, 1]
]

for i in range(1, len(a)):
    for r in range(5):
        for k in range(5):
            if a[i-1] == r: continue
            dp[i][a[i-1]][r] = min(dp[i][a[i-1]][r], dp[i-1][k][r] + mv[k][a[i-1]])
    for l in range(5):
        for k in range(5):
            if a[i-1] == l: continue
            dp[i][l][a[i-1]] = min(dp[i][l][a[i-1]], dp[i-1][l][k] + mv[k][a[i-1]])

print(min(*dp[n-1][a[max(n-2, 0)]],
          dp[n-1][0][a[max(n-2, 0)]],
          dp[n-1][1][a[max(n-2, 0)]],
          dp[n-1][2][a[max(n-2, 0)]],
          dp[n-1][3][a[max(n-2, 0)]],
          dp[n-1][4][a[max(n-2, 0)]])
    )