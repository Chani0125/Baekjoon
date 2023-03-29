import sys

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().strip().split()))

total = 0
now = 0
p.sort()

for i in p:
    total += now + i
    now += i

print(total)