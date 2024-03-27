import sys
from math import sqrt

input = sys.stdin.readline
lr = 10000
lambda_ = 0.0
iter = 10

def l2_dist(dot1, dot2):
    return sqrt((dot1[0] - dot2[0]) ** 2 + (dot1[1] - dot2[1]) ** 2)


n = int(input())
dots = [tuple(map(int, input().split())) for _ in range(n)]

x = sum(list(zip(*map(list, dots)))[0]) / n
y = sum(list(zip(*map(list, dots)))[1]) / n

iter1 = iter * 100
iter2 = 10
dist = [.0] * n
dx, dy = .0, .0

for epoch in range(iter1):
    if epoch % (iter1 // iter) == 0:
        lr = lr / 10
    
    for _ in range(iter2):
        for i in range(n):
            dist[i] = l2_dist((x, y), dots[i])
        tmp = 0
        for i in range(n):
            tmp += ((x - dots[i][0]) / dist[i]) if dist[i] else 0
        dx = tmp * (1 - lambda_) + dx * lambda_
        x = x - lr * dx
    
    for _ in range(iter2):
        for i in range(n):
            dist[i] = l2_dist((x, y), dots[i])
        tmp = 0
        for i in range(n):
            tmp += ((y - dots[i][1]) / dist[i]) if dist[i] else 0
        dy = tmp * (1 - lambda_) + dy * lambda_
        y = y - lr * dy

dist = 0
for dot in dots:
    dist += l2_dist((x, y), dot)
print(round(dist))