import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

dp = [[1] * n for i in range(n)]
for t in range(1, n):
    for i in range(n-t):
        dp[i][i+t] = int(a[i] == a[i+t] and dp[i+1][i+t-1])

m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])
