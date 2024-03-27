import sys

n, m = map(int, sys.stdin.readline().strip().split())
if m > n // 2:
    m = n - m
ans = 1
for i in range(m):
    ans *= n - i
    ans //= i + 1
print(ans)
