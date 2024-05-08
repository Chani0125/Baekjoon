import sys

input = sys.stdin.readline
n = int(input())
adj_mat = [list(map(int, input().split())) for _ in range(n)]
# if adj_mat == 0, then it is unreachable

INF = n * 1000000 + 1
dp = [[INF] * (1 << n) for _ in range(n)]

def tsp(cur, visited):
    # trivial case
    if visited == (1 << n) - 1:
        return adj_mat[cur][0] or INF
    
    # memoization case
    if dp[cur][visited] != INF:
        return dp[cur][visited]
    
    # recursive case
    for i in range(1, n):
        if adj_mat[cur][i] != 0 and visited & (1 << i) == 0:
            dp[cur][visited] = min(dp[cur][visited], tsp(i, visited | (1 << i)) + adj_mat[cur][i])
    dp[cur][visited] = min(dp[cur][visited], INF-1)
    
    return dp[cur][visited]

print(tsp(0, 1))
