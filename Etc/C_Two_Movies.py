import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    c = []
    
    p, q = 0, 0
    for i in range(n):
        if a[i] == 1:
            if b[i] == 1:
                c.append((1, 1))
            else:
                p += a[i]
        elif a[i] == -1:
            if b[i] == -1:
                c.append((-1, -1))
            else:
                q += b[i]
        else:
            if b[i] == 1:
                q += 1
    
    for x, y in c:
        if x == 1:
            if p < q:
                p += 1
            else:
                q += 1
        if x == -1:
            if p > q:
                p -= 1
            else:
                q -= 1
        
    print(min(p, q))