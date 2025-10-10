import sys

input = sys.stdin.readline
n = int(input())
v = [list(map(int, list(input().strip()))) for _ in range(n)]

# ans = ''

def quard(n, x, y):
    if n == 1:
        # print('test', n, x, y)
        print(v[x][y], end='')
        return

    # global ans
    
    s = sum([sum(v[i][y:y+n]) for i in range(x, x+n)])
    # print('\nTest', n, x, y, s)

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

    # print(n, x, y, s, a, b, c, d)
    # print(a, b, c, d, sep='')    
    
    # ans += '('
    # ans += 
    
    # print('(', end='')
    # print(a if a != 2 else '', end='')
    # print(b if b != 2 else '', end='')
    # print(c if c != 2 else '', end='')
    # print(d if d != 2 else '', end='')
    
    # print(')', end='')
    # return 2

quard(n, 0, 0)

# print(ans)
    