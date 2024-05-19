import sys

input = sys.stdin.readline
n = int(input())
v = [tuple(map(int, input().split())) for _ in range(n)]

ZERO = 1e-9
x, y = sum(list(zip(*v))[0]) / n, sum(list(zip(*v))[1]) / n

def cost():
    res, i = -1, -1
    for idx, (a, b) in enumerate(v):
        tmp = ((x - a) ** 2 + (y - b) ** 2) ** 0.5
        if tmp > res:
            res = tmp
            i = idx
    return i, res

lr = cost()[1]
epoch_num = 4000
i, d = -1, 0

for epoch in range(epoch_num):
    pi, pd = i, d
    i, d = cost()
    dx = (x - v[i][0]) / (d if d else ZERO)
    dy = (y - v[i][1]) / (d if d else ZERO)
    x = x - dx * lr
    y = y - dy * lr
    
    if epoch % 250 == 0:
        if pi == i and abs(d - pd) < 1e-3:
            break
        lr /= 3.16

print(f'{round(cost()[1]*2, 2):.2f}')
# print(f'{cost()[1]*2:.2f}')