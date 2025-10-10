import sys

sys.setrecursionlimit(100000)

n, m = map(int, sys.stdin.readline().split())
a = [list(sys.stdin.readline().strip()) for _ in range(n)]
for x, i in enumerate(a):
    for y, j in enumerate(i):
        if j == 'R':
            red = x, y
            a[x][y] = '.'
        if j == 'B':
            blue = x, y
            a[x][y] = '.'
        if j == 'O': o = x, y

def move(depth, b, r):
    if depth > 10: return False, depth
    
    res = []
    x, y = b
    p, q = r
    while a[x+1][y] == '.' and (not x+1 == p or not y == q): x += 1
    while a[p+1][q] == '.' and (not x == p+1 or not y == q): p += 1
    while a[x+1][y] == '.' and (not x+1 == p or not y == q): x += 1
    if not (x+1 == o[0] and y == o[1]):
        if p+1 == o[0] and q == o[1]:
            if not (x+2 == o[0] and y == o[1]):
                return True, depth
        else:
            if not ((x, y) == b and (p, q) == r):
                ans = move(depth+1, (x, y), (p, q))
                if ans[0]: res.append(ans[1])
        
    x, y = b
    p, q = r
    while a[x-1][y] == '.' and (not x-1 == p or not y == q): x -= 1
    while a[p-1][q] == '.' and (not x == p-1 or not y == q): p -= 1
    while a[x-1][y] == '.' and (not x-1 == p or not y == q): x -= 1
    if not (x-1 == o[0] and y == o[1]):
        if p-1 == o[0] and q == o[1]:
            if not (x-2 == o[0] and y == o[1]):
                return True, depth
        else:
            if not ((x, y) == b and (p, q) == r):
                ans = move(depth+1, (x, y), (p, q))
                if ans[0]: res.append(ans[1])
            
    x, y = b
    p, q = r
    while a[x][y+1] == '.' and (not x == p or not y+1 == q): y += 1
    while a[p][q+1] == '.' and (not x == p or not y == q+1): q += 1
    while a[x][y+1] == '.' and (not x == p or not y+1 == q): y += 1
    if not (x == o[0] and y+1 == o[1]):
        if p == o[0] and q+1 == o[1]:
            if not (x == o[0] and y+2 == o[1]):
                return True, depth
        else:
            if not ((x, y) == b and (p, q) == r):
                ans = move(depth+1, (x, y), (p, q))
                if ans[0]: res.append(ans[1])
            
    x, y = b
    p, q = r
    while a[x][y-1] == '.' and (not x == p or not y-1 == q): y -= 1
    while a[p][q-1] == '.' and (not x == p or not y == q-1): q -= 1
    while a[x][y-1] == '.' and (not x == p or not y-1 == q): y -= 1
    if not (x == o[0] and y-1 == o[1]):
        if p == o[0] and q-1 == o[1]:
            if not (x == o[0] and y-2 == o[1]):
                return True, depth
        else:
            if not ((x, y) == b and (p, q) == r):
                ans = move(depth+1, (x, y), (p, q))
                if ans[0]: res.append(ans[1])
    
    if res: return True, min(res)
    return False, depth

res = move(1, blue, red)
if res[0]: print(res[1])
else: print(-1)