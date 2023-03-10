t = int(input())
for _ in range(t):
    n = int(input())
    c = {}
    for _ in range(n):
        name, kind = input().split()
        if kind in c:
            c[kind] += 1
        else:
            c[kind] = 1
    ans = 1
    for i in c.values():
        ans *= i + 1
    ans -= 1
    print(ans)