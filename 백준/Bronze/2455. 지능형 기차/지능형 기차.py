p, q = 0, 0
for _ in range(4):
    a, b = map(int, input().split())
    p += b - a
    q = max(q, p)
print(q)