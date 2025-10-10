import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

a = deque(list(range(n)))
b = [0] * n
for i in range(1, n+1):
    for _ in range(i):
        a.append(a.popleft())
    b[a.popleft()] = i
print(*b)
