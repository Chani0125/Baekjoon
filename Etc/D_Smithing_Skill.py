import sys

input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

v = sorted(list(zip(a, b)), key=lambda x: x[0]-x[1])

exp = 0
for ai, bi in v:
    for i in range(len(c)):
        if c[i] >= ai:
            times = (c[i] - ai) // (ai - bi) + 1
            exp += times * 2
            c[i] -= times * (ai - bi)

print(exp)
