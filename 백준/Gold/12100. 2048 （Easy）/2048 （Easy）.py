import sys
import copy

def move(v, dir):
    n = len(v)
    m = v[:]
    
    if dir == 1:
        m = list(map(list, zip(*m)))
    elif dir == 2:
        m = [i[::-1] for i in m[:]]
    elif dir == 3:
        m = [i[::-1] for i in list(map(list, zip(*m)))]
        
    for i in range(n):
        for j in range(n-1):
            if m[i][j] == 0:
                for k in range(j+1, n):
                    if m[i][k] != 0:
                        m[i][j] = m[i][k]
                        m[i][k] = 0
                        break
            for k in range(j+1, n):
                if m[i][j] == m[i][k]:
                    m[i][j] <<= 1
                    m[i][k] = 0
                    break
                elif m[i][k] != 0:
                    break
            
    return m          
 

n = int(sys.stdin.readline())
v = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
vv = [v]

for _ in range(5):
    for v in vv[:]:
        for i in range(4):
            vv.append(move(copy.deepcopy(v), i))
        vv.pop(0)

ans = 0
for v in vv:
    for i in v:
        ans = max(ans, max(i))
    
print(ans)
