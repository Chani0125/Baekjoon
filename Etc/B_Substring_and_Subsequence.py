import sys

input = sys.stdin.readline
n = int(input())
s = [input().strip() for _ in range(n*2)]

for t in range(n):
    a = s[t*2+1]
    b = s[t*2]
    v = [0] * len(a)
    
    for i in range(len(a)):
        p = 0
        for j in range(len(b)):
            if i+p < len(a) and a[i+p] == b[j]:
                p += 1
        v[i] = p
    
    print(len(a) + len(b) - max(v))