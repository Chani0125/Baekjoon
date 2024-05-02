import sys

input = sys.stdin.readline
n = int(input())
a = [tuple(map(int, input().split())) for _ in range(n)]

def cross(p, q):
    a1, a2 = ccw(p[0:2], p[2:4], q[0:2]), ccw(p[0:2], p[2:4], q[2:4])
    b1, b2 = ccw(q[0:2], q[2:4], p[0:2]), ccw(q[0:2], q[2:4], p[2:4])
    if a1 == a2 == b1 == b2 == 0:
        c0, c1, c2, c3 = p[0], p[2], q[0], q[2]
        c4, c5, c6, c7 = p[1], p[3], q[1], q[3]
        if c0 > c1: c0, c1 = c1, c0
        if c2 > c3: c2, c3 = c3, c2
        if c4 > c5: c4, c5 = c5, c4
        if c6 > c7: c6, c7 = c7, c6
        if c0 <= c2 <= c1 or c0 <= c3 <= c1 or c2 <= c0 <= c3 or c2 <= c1 <= c3:
            if c4 <= c6 <= c5 or c4 <= c7 <= c5 or c6 <= c4 <= c7 or c6 <= c5 <= c7:
                return True
        return False
    return a1*a2 <= 0 and b1*b2 <= 0

def ccw(p, q, r):
    return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])

class union_find:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.parent[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1

u = union_find(n)
for i in range(n):
    for j in range(i+1, n):
        if cross(a[i], a[j]):
            u.union(i, j)

cnt = 0
cnt_list = [0] * n
for i in range(n):
    p = u.find(i)
    cnt_list[p] += 1
    if p == i:
        cnt += 1
print(cnt)
print(max(cnt_list))
