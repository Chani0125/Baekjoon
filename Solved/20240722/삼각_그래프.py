import sys

input = sys.stdin.readline
n = int(input())
t = 1

while n:
    g = [list(map(int, input().split())) for _ in range(n)]

    dp = [[0, 0, 0] for _ in range(n)]
    dp[0] = [1000000, g[0][1], g[0][1]+g[0][2]]
    for i in range(1, n):
        dp[i][0] = min(dp[i-1][0], dp[i-1][1]) + g[i][0]
        dp[i][1] = min(dp[i][0], dp[i-1][0], dp[i-1][1], dp[i-1][2]) + g[i][1]
        dp[i][2] = min(dp[i][1], dp[i-1][1], dp[i-1][2]) + g[i][2]

    # print(*dp, sep='\n')
    print(f'{t}. {dp[n-1][1]}')
    
    n = int(input())
    t += 1

