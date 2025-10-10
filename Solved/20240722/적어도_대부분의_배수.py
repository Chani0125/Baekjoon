a = [*map(int, input().split())]
ans = 10000000000

def gcd(a, b):
    while b: a, b = b, a%b
    return a

def lcm(a, b):
    return a*b // gcd(a, b)

from itertools import combinations

for i, j, k in combinations(a, 3):
    ans = min(ans, lcm(lcm(i, j), k))

print(ans)