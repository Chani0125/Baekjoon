t = int(input())
for i in range(t):
    n = int(input())
    c = {}
    ct = []
    for j in range(n):
        a, b = input().split()
        c[a] = b
        if b not in c:
            ct.append(b)

