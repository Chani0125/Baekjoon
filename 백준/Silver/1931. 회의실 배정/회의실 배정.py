import sys

input = sys.stdin.readline

n = int(input())
v = [tuple(map(int, input().split())) for _ in range(n)]

v.sort(key=lambda x: (x[1], x[0]))

ans = 1
last = v[0][1]
for s, e in v[1:]:
    if s >= last:
        last = e
        ans += 1
print(ans)