import sys
from math import sqrt

def l2_dist(dot1, dot2):
    return sqrt((dot1[0] - dot2[0]) ** 2 + (dot1[1] - dot2[1]) ** 2 + (dot1[2] - dot2[2]) ** 2)

lr = 1000000000
lambda_ = 0.5

dots = [tuple(map(int, sys.stdin.readline().split())) for _ in range(3)]

x = (dots[0][0] + dots[1][0] + dots[2][0]) / 3
y = (dots[0][1] + dots[1][1] + dots[2][1]) / 3
z = (dots[0][2] + dots[1][2] + dots[2][2]) / 3
dx, dy, dz = 0, 0, 0

iter1 = 1400
iter2 = 100
d = [.0, .0, .0]
for epoch in range(iter1):
    if epoch % (iter1 // 14) == 0:
        lr = lr / 10
    
    for _ in range(iter2):
        for i in range(3):
            d[i] = l2_dist((x, y, z), dots[i])
        dx = (\
            (((x - dots[0][0]) / d[0]) if d[0] else 0) +\
            (((x - dots[1][0]) / d[1]) if d[1] else 0) +\
            (((x - dots[2][0]) / d[2]) if d[2] else 0)) \
            * (1 - lambda_) + dx * lambda_
        x = x - lr * dx
         
    for _ in range(iter2):
        for i in range(3):
            d[i] = l2_dist((x, y, z), dots[i])
        dy = (\
            (((y - dots[0][1]) / d[0]) if d[0] else 0) +\
            (((y - dots[1][1]) / d[1]) if d[1] else 0) +\
            (((y - dots[2][1]) / d[2]) if d[2] else 0)) \
            * (1 - lambda_) + dy * lambda_
        y = y - lr * dy
    
    for _ in range(iter2): 
        for i in range(3):
            d[i] = l2_dist((x, y, z), dots[i])
        dz = (\
            (((z - dots[0][2]) / d[0]) if d[0] else 0) +\
            (((z - dots[1][2]) / d[1]) if d[1] else 0) +\
            (((z - dots[2][2]) / d[2]) if d[2] else 0)) \
            * (1 - lambda_) + dz * lambda_
        z = z - lr * dz
    
dist = 0
for dot in dots:
    dist += l2_dist((x, y, z), dot)
print(f'{dist:.6f}')
