import sys
from math import sqrt

input = sys.stdin.readline
lambda_ = 0.2

iter_a = 8
iter1 = iter_a * 50

def l2_dist(dot1, dot2):
    return sqrt((dot1[0] - dot2[0]) ** 2 + (dot1[1] - dot2[1]) ** 2)


t = int(input())
for _ in range(t):
    n = int(input())
    dots = [tuple(map(float, input().split())) for _ in range(n)]
    max_ = 0
    for a, b in dots:
        max_ = max(max_, abs(a), abs(b))
    lr = max_
    
    x = sum(list(zip(*map(list, dots)))[0]) / n
    y = sum(list(zip(*map(list, dots)))[1]) / n

    dx, dy = .0, .0
    dist = [.0] * n
    
    for epoch in range(1, iter1):
        if epoch % (iter1 // iter_a) == 0:
            lr = lr / 10
        
        for i in range(n):
            dist[i] = l2_dist((x, y), dots[i])
        
        t1, t2 = .0, .0
        for i in range(n):
            t1 += ((x - dots[i][0]) / dist[i]) if dist[i] else 10e-7
            t2 += ((y - dots[i][1]) / dist[i]) if dist[i] else 10e-7
        dx = dx * lambda_ + t1 * (1 - lambda_)
        dy = dy * lambda_ + t2 * (1 - lambda_)
        
        x = x - lr * dx
        y = y - lr * dy
        
    print(x, y)
