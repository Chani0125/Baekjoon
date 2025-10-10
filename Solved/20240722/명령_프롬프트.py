import sys

input = sys.stdin.readline

n = int(input())
a = list(input().strip())
for _ in range(n-1):
    b = list(input().strip())
    for i in range(len(a)):
        if a[i] != b[i]: a[i] = '?'
print(*a, sep='')