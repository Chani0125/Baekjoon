import sys

n = int(input())
a = list(map(int, input().split()))

from collections import deque

now = 1
s = deque()
for i in range(n):
    while s and s[-1] == now:
        s.pop()
        now += 1
    
    if a[i] == now:
        now += 1
    else:
        s.append(a[i])

while s and s[-1] == now:
    s.pop()
    now += 1

if s:
    print('Sad')
else:
    print('Nice')