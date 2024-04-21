import sys
sys.setrecursionlimit(10**6)


def find_baechu(x, y, i):
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for a, b in d:
        if x+a < 0 or y+b < 0:
            continue
        try:
            if baechu[x+a][y+b] == 1:
                baechu[x+a][y+b] = 0
                find_baechu(x+a, y+b, i)
            else:
                continue
        except IndexError:
            continue
    return 0


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    baechu = [[0 for i in range(n)] for j in range(m)]
    for i in range(k):
        x, y = map(int, input().split())
        baechu[x][y] = 1
    num_baechu = 0
    idx = 0
    for i in range(len(baechu)):
        for j in range(len(baechu[i])):
            if baechu[i][j] == 1:
                num_baechu += 1
                baechu[i][j] = 0
                find_baechu(i, j, idx)
                idx += 1
    print(num_baechu)
