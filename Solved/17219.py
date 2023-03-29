import sys

n, m = map(int, sys.stdin.readline().strip().split())
a = [tuple(sys.stdin.readline().strip().split()) for _ in range(n)]
b = [sys.stdin.readline().strip() for _ in range(m)]

pw = {}
for k, v in a:
    pw[k] = v

for i in b:
    print(pw[i])
