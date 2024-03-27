import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

dp = [{i} for i in range(n)]
for i in range(1, n):
    for j in range(i):
        for k in range((i-j+1)//2):
            if a[j] != a[i-k]:
                break
        else:
            dp[i].add(j)


m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    print(int(s-1 in dp[e-1]))
