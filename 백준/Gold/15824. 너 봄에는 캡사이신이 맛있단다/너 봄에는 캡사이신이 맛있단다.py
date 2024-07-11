import sys

input = sys.stdin.readline
n = int(input())
v = sorted(list(map(int, input().split())))

a = 0
for i in range(n):
    a += ((1<<i)%1000000007 - (1<<(n-1-i))%1000000007) % 1000000007 * v[i]
    a %= 1000000007
print(a)