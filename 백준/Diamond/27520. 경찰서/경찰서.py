import sys

input = sys.stdin.readline
n = int(input())
road = [tuple(map(int, input().split())) for _ in range(n)]

ZERO = 1e-6

def dist(x, y):
    res, i = -1, -1
    for idx, (a, b, c) in enumerate(road):
        d = abs(a*x + b*y + c) / ((a**2 + b**2) ** 0.5)
        if res < d:
            res = d
            i = idx
    return i, res

def dist_3(x, y):
    p1, p2, p3 = (-1, -1), (-1, -1), (-1, -1)
    for idx, (a, b, c) in enumerate(road):
        d = abs(a*x + b*y + c) / ((a**2 + b**2) ** 0.5)
        if d > p1[1]:
            p1, p2, p3 = (idx, d), p1, p2
        elif d > p2[1]:
            p2, p3 = (idx, d), p2
        elif d > p3[1]:
            p3 = (idx, d)
    return p1, p2, p3

def d_dist(x, y, num):
    a, b, c = road[num]
    p = (a**2 + b**2) ** 0.5
    q = a*x + b*y + c
    res_x, res_y = a * q, b * q
    res_x /= p
    res_y /= p
    res_x /= abs(q) if q else ZERO
    res_y /= abs(q) if q else ZERO
    return res_x, res_y

def intersection(n1, n2):
    a1, b1, c1 = road[n1]
    a2, b2, c2 = road[n2]
    res_x = (b1*c2 - b2*c1) / (a1*b2 - a2*b1)
    res_y = (a2*c1 - a1*c2) / (a1*b2 - a2*b1)
    return res_x, res_y

def lenth(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2) ** 0.5

def incenter(n1, n2, n3):
    a = intersection(n1, n2)
    b = intersection(n2, n3)
    c = intersection(n3, n1)
    
    ab = lenth(a, b)
    bc = lenth(b, c)
    ca = lenth(c, a)
    
    if ab + bc + ca == 0: return a
    
    res_x = (ab*c[0] + bc*a[0] + ca*b[0]) / (ab + bc + ca)
    res_y = (ab*c[1] + bc*a[1] + ca*b[1]) / (ab + bc + ca)
    
    return res_x, res_y

if n < 3:
    print(0)
    exit()    
if n == 3:
    x, y = incenter(0, 1, 2)
    a, b, c = road[0]
    d = abs(a*x + b*y + c) / ((a**2 + b**2) ** 0.5)
    print(d)
    exit()

x, y = .0, .0

alpha = 0.5
for epoch in range(100):
    p1, p2, p3 = dist_3(x, y)
    dx, dy = incenter(p1[0], p2[0], p3[0])
    x = x * (1 - alpha) + dx * alpha
    y = y * (1 - alpha) + dy * alpha
    
lr = dist(x, y)[1] * 0.1

i, d = -1, ZERO
    
# epoch_num = 3000
# for epoch in range(1, epoch_num+1):

alpha = 0.01
while lr > ZERO * 0.1:
    pi, pd = i, d
    i, d = dist(x, y)
    
    dx, dy = d_dist(x, y, i)
    x = x - dx * lr
    y = y - dy * lr

    if lr > ZERO:
        p1, p2, p3 = dist_3(x, y)
        dx, dy = incenter(p1[0], p2[0], p3[0])
        x = x * (1 - alpha) + dx * alpha
        y = y * (1 - alpha) + dy * alpha
    # if pi == i and abs(d - pd) / pd < ZERO:
    #     break
    
    # if epoch % 1 == 0:
    lr *= 0.99
# else:
#     print('NO BREAK')

alpha = 0.01
for epoch in range(500):
    p1, p2, p3 = dist_3(x, y)
    dx, dy = incenter(p1[0], p2[0], p3[0])
    x = x * (1 - alpha) + dx * alpha
    y = y * (1 - alpha) + dy * alpha

print(dist(x, y)[1])