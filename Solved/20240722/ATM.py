import sys

input = sys.stdin.readline
n = int(input())
p = list(map(int, input().split()))

p.sort()
q = [p[0]]
for i in range(1, n):
    q.append(q[i-1] + p[i])
print(sum(q))