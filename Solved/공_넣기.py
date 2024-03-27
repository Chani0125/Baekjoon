import sys

n, m = map(int, sys.stdin.readline().split())
basket = [0] * n

for _ in range(m):
    i, j, k = map(int, sys.stdin.readline().split())
    for idx in range(i-1, j):
        basket[idx] = k

for i in basket:
    print(i, end=' ')