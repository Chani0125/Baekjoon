import sys
from math import sqrt

t = int(sys.stdin.readline())
for _ in range(t):
    x, y = map(int, sys.stdin.readline().strip().split())
    d = y - x
    r = sqrt(1 + 4 * d)
    n = (-1 + int(r)) // 2
    if r == int(r):
        n -= 1
    if d > (n + 1) ** 2:
        print(2 * n + 2)
    else:
        print(2 * n + 1)
