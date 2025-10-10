import sys
from bisect import bisect_left, bisect_right


input = sys.stdin.readline
n, k = map(int, input().split())

while n:
    a = list(map(int, input().split()))

    b = []
    c = [0]
    t = 1
    for i in range(1, n):
        if a[i] - a[i-1] != 1:
            b.append(t)
            c.append(c[-1] + t)
            t = 0
        t += 1
    b.append(t)
    c.append(c[-1] + t)
    # print(b)
    # print(c)

    d = bisect_right(c, bisect_left(a, k))
    # print(d)
    
    v = [[b[0]]]
    p = len(v[0])
    q = p + sum(v[0])
    while q <= len(b): 
        v.append(b[p:q])
        p = q
        q += sum(v[-1])
    v.append(b[p:] + [0] * (q-len(c)+1))
    
    t = 0
    for i, x in enumerate(v):
        for j, y in enumerate(x):
            t += 1
            if t == d:
                pos = (i, j)
                break
    
    print(*v, sep='\n')
    print(pos)
    
    if pos[0] == 0:
        print(0)
    else:
        e = [0]
        for x in v[pos[0]-1]:
            e.append(e[-1] + x)
        print(e)
        
    f = bisect_right(e, pos[1]) - 1
    # print(f)
    
    ans = sum(v[pos[0]][e[f]:e[f+1]]) - v[pos[0]][pos[1]]
    print(ans)
    
    n, k = map(int, input().split())
    

