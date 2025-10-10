import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s, t = map(int, input().split())
    
    ans = 0
    while n*s >= t*2:
        if n % 2 == 0:
            n >>= 1
            ans += t
        else:
            n -= 1
            ans += s
    print(ans + n*s)