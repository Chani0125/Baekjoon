T = int(input())
for i in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    circle = []
    move = 0
    for j in range(n):
        tmp = list(map(int, input().split()))
        if (x1-tmp[0])**2 + (y1-tmp[1])**2 < tmp[2]**2:
            tmp.append(1)
        else:
            tmp.append(0)
        if (x2-tmp[0])**2 + (y2-tmp[1])**2 < tmp[2]**2:
            tmp.append(1)
        else:
            tmp.append(0)
        circle.append(tmp)
    for i in circle:
        if not i[3] == i[4]:
            move += 1
    print(move)

