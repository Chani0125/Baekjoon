import sys

input = sys.stdin.readline
n = int(input())

ZERO = 1e-9

def cost(x, y):
    res, i = -1, -1
    for idx, (a, b) in enumerate(v):
        tmp = ((x - a) ** 2 + (y - b) ** 2) ** 0.5
        if tmp > res:
            res = tmp
            i = idx
    return i, res

for k in range(n):
    a0, a1, a2, a3, a4, a5 = map(int, input().split())
    v = [(a0, a1), (a2, a3), (a4, a5)]
    x, y = sum(list(zip(*v))[0]) / n, sum(list(zip(*v))[1]) / n

    lr = cost(x, y)[1]
    epoch_num = 4000
    i, d = -1, 0

    for epoch in range(epoch_num):
        pi, pd = i, d
        i, d = cost(x, y)
        dx = (x - v[i][0]) / (d if d else ZERO)
        dy = (y - v[i][1]) / (d if d else ZERO)
        x = x - dx * lr
        y = y - dy * lr
        
        if epoch % 250 == 0:
            if pi == i and (abs(d - pd) < 1e-4):
                break
            lr /= 3.16

    print(f'Case #{k+1}: {x:.2f} {y:.2f}')