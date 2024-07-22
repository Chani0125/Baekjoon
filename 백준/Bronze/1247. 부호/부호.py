import sys

input = sys.stdin.readline
for _ in range(3):
    n = int(input())
    s = sum([int(input()) for _ in range(n)])
    if s == 0:
        print('0')
    elif s > 0:
        print('+')
    else:
        print('-')