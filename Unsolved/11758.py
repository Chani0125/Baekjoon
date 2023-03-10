p = [list(map(int, input().split())) for _ in range(3)]
d = [(p[i+1][0] - p[i][0], p[i+1][1] - p[i][1]) for i in range(2)]
a = []
for dx, dy in d:
    if dx > 0 and dy == 0:
        a.append(0)
    elif dx > 0 and dy > 0:
        a.append(1)
    elif dx == 0 and dy > 0:
        a.append(2)
    elif dx < 0 and dy > 0:
        a.append(3)
    elif dx < 0 and dy == 0:
        a.append(4)
    elif dx < 0 and dy < 0:
        a.append(5)
    elif dx == 0 and dy < 0:
        a.append(6)
    elif dx > 0 and dy < 0:
        a.append(7)
if 0 < (a[1] - a[0]) % 8 < 4:
    print(1)
elif 4 < (a[1] - a[0]) % 8 < 8:
    print(-1)
else:
    minus = 0
    for i in range(2):
        if d[i][1] < 0:
            minus += 1
    if d[0][0] * d[1][1] < d[0][1] * d[1][0]:
        if minus == 1:
            print(-1)
        else:
            print(1)
    elif d[0][0] * d[1][1] > d[0][1] * d[1][0]:
        if minus == 1:
            print(1)
        else:
            print(-1)
    else:
        print(0)
