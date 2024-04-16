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
b = a
# b = []

# for i in range(k):
#     for j in range(k):
#         if i != j and a[i] % a[j] == 0:
#             break
#     else:
#         b.append(a[i])
# b.sort()

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