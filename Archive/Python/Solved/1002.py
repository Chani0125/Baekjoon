T = int(input())
for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        d = 0
    elif x1 == x2:
        d = abs(y1 - y2)
    elif y1 == y2:
        d = abs(x1 - x2)
    else:
        d = ((x1-x2)**2 + (y1-y2)**2) ** 0.5

    if d == 0 and r1 == r2:
        print(-1)
        continue
    elif d == 0:
        print(0)
        continue

    if r1 + r2 > d > abs(r1 - r2):
        print(2)
        continue
    elif d < abs(r1 - r2):
        print(0)
        continue
    elif d > r1 + r2:
        print(0)
        continue
    else:
        print(1)
