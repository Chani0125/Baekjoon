import sys

input = sys.stdin.readline
a = list(input().strip())
n = len(a)

dp = [[1] * n for _ in range(n)]
for t in range(1, n):
    for i in range(n-t):
        if a[i] == a[i+t] and dp[i+1][i+t-1] == 1:
            continue
        dp[i][i+t] = 0
        # dp[i][i+t] = dp[i][i] + dp[i+1][i+t]
        # for j in range(1, t):
        #     dp[i][i+t] = min(dp[i][i+t], dp[i][i+j] + dp[i+j+1][i+t])

v = [i for i in range(1, n+1)]
for i in range(n):
    if dp[0][i]:
        v[i] = 1
        continue
    for j in range(i+1):
        if dp[j][i]: v[i] = min(v[i], v[j-1] + 1)
        # v[i] = min(v[i], dp[0][j] + dp[j+1][i])

print(v[n-1])
# print(v)
# print(*dp, sep='\n')
# print(slice_min(0, n-1))