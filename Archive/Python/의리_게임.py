import sys

input = sys.stdin.readline

n, q = map(int, input().split())
m = [int(input()) for _ in range(n)]
v = [0, ] * n
s = [0]
for i in range(n):
    s.append(s[-1] + m[i])

from bisect import bisect_left

for _ in range(q):
    a = list(map(int, input().split()))
    if a[0] == 1:
        for i in range(a[1]-1, n):
            if v[i] == m[i]:
                continue
            elif a[2] > m[i] - v[i]:
                a[2] -= m[i] - v[i]
                v[i] = m[i]
            else:
                v[i] += a[2]
                break
    else:
        print(v[a[1]-1])