import sys

input = sys.stdin.readline
n, m = map(int, input().split())
a = list(range(1, n+1))
for _ in range(m):
    s, l = map(int, input().split())
    for idx, var in enumerate(a[s-1:l][::-1]):
        a[idx+s-1] = var
print(*a)