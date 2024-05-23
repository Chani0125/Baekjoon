import sys

input = sys.stdin.readline
n = int(input())
c = [int(input()) for _ in range(n)]

for i in range(len(c)):
    print(c[i] // 25, end=' ')
    c[i] %= 25
    print(c[i] // 10, end=' ')
    c[i] %= 10
    print(c[i] // 5, end=' ')
    c[i] %= 5
    print(c[i])
    