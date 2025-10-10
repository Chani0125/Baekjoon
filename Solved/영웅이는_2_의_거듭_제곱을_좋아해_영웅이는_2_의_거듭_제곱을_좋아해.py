import sys

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))

b = 0
for i in a:
    b ^= i

c = [b]
for i in a:
    c.append(b^i)

print(str(max(c)) * 2)