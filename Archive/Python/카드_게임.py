import sys

def card(start, end, dp, t, n) -> int:
    n_card = end - start
    if n_card < 0:
        return 0
    if n_card == 0:
        return t[start]
    
    if ((n - n_card) % 2 == 0):
        dp[start][end] = max(card(start+1, end, dp, t, n) + t[start], card(start, end-1, dp, t, n) + t[end])
        return dp[start][end]
    else:
        dp[start][end] = min(card(start+1, end, dp, t, n) + t[start], card(start, end-1, dp, t, n) + t[end])
        return dp[start][end]
    

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    t = list(map(int, sys.stdin.readline().split()))
    
    dp = [[0] * n for _ in range(n)]
    print(card(0, n-1, dp, t, n))
    print(*dp, sep='\n')