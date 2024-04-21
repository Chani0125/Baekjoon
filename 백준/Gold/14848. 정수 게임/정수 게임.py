import sys
from itertools import combinations

input = sys.stdin.readline

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)


n, k = map(int, input().split())
a = list(map(int, input().split()))
b = set()

for i, j in combinations(a, 2):
    if i % j == 0:
        b.add(j)
    elif j % i == 0:
        b.add(i)
    else:
        b.add(i)
        b.add(j)
b = list(b)

if b[0] == 1:
    print(0)
    exit()

ans = n
for i in b:
    ans -= n // i
for i in range(2, len(b)+1):
    for c in combinations(b, i):
        l = c[0]
        for j in c[1:]:
            l = lcm(l, j)
        ans += (-1 if i % 2 else 1) * (n // l)
print(ans)