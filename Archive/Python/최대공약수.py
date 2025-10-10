import sys

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

c = dict()
for i in range(n):
    for j in range(m):
        g = gcd(a[i], b[j])
        if g != 1:
            if g in c:
                c[g] += 1
            else:
                c[g] = 1

d = 1
for i in c:
    d *= i ** c[i]

ans = 1
if n < m:
    for i in range(n):
        ans *= gcd(a[i], d)
else:
    for i in range(m):
        ans *= gcd(b[i], d)
print(str(ans)[-9:])