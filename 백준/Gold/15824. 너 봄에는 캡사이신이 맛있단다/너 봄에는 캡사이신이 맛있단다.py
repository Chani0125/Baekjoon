import sys

input = sys.stdin.readline
n = int(input())
v = sorted(list(map(int, input().split())))
u = [v[-1-i]-v[i] for i in range((n+1)>>1)]

pow2 = [1]
for _ in range(300000):
    pow2.append((pow2[-1] << 1) % 1000000007)

a = 0
for i in range((n+1)>>1):
    a += (pow2[n-1-i]-pow2[i]) * u[i]
    a %= 1000000007
if a < 0:
    a += 1000000007
print(a)