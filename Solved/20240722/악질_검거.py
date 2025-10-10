import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = [input().split() for _ in range(n)]
b = [0] * n
c = set()
for i, arr in enumerate(a):
    p, q = 0, 0
    for k in arr[:-1]:
        if k == '*':
            p = max(p, q)
            q = 0
        else:
            q += 1
    b[i] = max(p, q)
    c.add(b[i])
print(len(c))
for i in range(n):
    print(b[i], a[i][m])
    