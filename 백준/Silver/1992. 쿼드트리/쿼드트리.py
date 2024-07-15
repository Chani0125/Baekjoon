import sys

input = sys.stdin.readline
n = int(input())
v = [list(map(int, list(input().strip()))) for _ in range(n)]

def quard(n, x, y):
    if n == 1:
        print(v[x][y], end='')
        return

    s = sum([sum(v[i][y:y+n]) for i in range(x, x+n)])

    if s == 0:
        print(0, end='')
        return
    if s == n**2:
        print(1, end='')
        return
    
    print('(', end='')
    quard(n>>1, x, y)
    quard(n>>1, x, y + (n>>1))
    quard(n>>1, x + (n>>1), y)
    quard(n>>1, x + (n>>1), y + (n>>1))
    print(')', end='')

quard(n, 0, 0)

    