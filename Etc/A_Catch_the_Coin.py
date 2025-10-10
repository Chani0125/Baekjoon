import sys

input = sys.stdin.readline
n = int(input())
v = [map(int, input().split()) for _ in range(n)]
for x, y in v:
    print('YES') if y >= -1 else print('NO')