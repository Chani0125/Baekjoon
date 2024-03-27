import sys

n, m = map(int, sys.stdin.readline().split())
comp = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in comp:
    print(f'{i}')

