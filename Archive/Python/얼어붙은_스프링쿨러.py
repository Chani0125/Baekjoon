import sys

input = sys.stdin.readline

while True:
    try:    n, c = map(int, input().split())
    except: break

    m = [[0] * (n+1) for _ in range(n+1)]
    for _ in range(n-1):
        u, v, w = map(int, input().split())
    