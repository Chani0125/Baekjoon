import sys

input = sys.stdin.readline
n = int(input())
print('Gnomes:')

for _ in range(n):
    a = list(map(int, input().split()))
    b = sorted(a)
    if a == b or a == b[::-1]:
        print('Ordered')
    else:
        print('Unordered')