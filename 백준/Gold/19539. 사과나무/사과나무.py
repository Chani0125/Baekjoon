import sys

input = sys.stdin.readline
n = int(input())
h = list(map(int, input().split()))

sh = sum(h)
one = sum(i % 2 for i in h)

if sh % 3:
    print('NO')
elif one > sh // 3:
    print('NO')
else:
    print('YES')
