import sys
from functools import cmp_to_key
from collections import deque

input = sys.stdin.readline
n = int(input())
v = [tuple(map(int, input().split())) for _ in range(n)]

def ccw(a, b, c):
    return (a[0]*b[1] + b[0]*c[1] + c[0]*a[1]) - (a[1]*b[0] + b[1]*c[0] + c[1]*a[0])

v.sort(key=lambda x: (x[1], x[0]))
v = [(x-v[0][0], y-v[0][1]) for x, y in v[:]]

def compare(a, b):
    t = ccw(a, (0, 0), b)
    if t > 0: return 1
    if t < 0: return -1
    if a[1] < b[1]: return -1
    if a[1] > b[1]: return 1
    if a[0] < b[0]: return -1
    return 1

v.sort(key=cmp_to_key(compare))

s = deque()
s.append(0)
s.append(1)
nxt = 2

while nxt < n:
    while len(s) >= 2:
        a, b = s.pop(), s[-1]
        if ccw(v[b], v[a], v[nxt]) > 0:
            s.append(a)
            break
    s.append(nxt)
    nxt += 1

print(len(s))