def NQueen(c, b, n, depth, s):
    if depth == n:
        return 1
    cnt = 0
    d = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
    for i in range(s, n):
        if c[0][i]:
            continue
        for j in range(n):
            if c[1][j]:
                continue
            tmp = True
            for x, y in d:
                if tmp:
                    k = 1
                    dx, dy = i + x, j + y
                    while 0 <= dx < n and 0 <= dy < n:
                        if b[dx][dy]:
                            tmp = False
                            break
                        k += 1
                        dx, dy = i + x * k, j + y * k
                else:
                    break
            if tmp:
                b[i][j] = True
                c[0][i] = True
                c[1][j] = True
                cnt += NQueen(c, b, n, depth+1, i+1)
                b[i][j] = False
                c[0][i] = False
                c[1][j] = False

    return cnt


n = int(input())
b = [[False for _ in range(n)] for _ in range(n)]
c = [[False for _ in range(n)] for _ in range(2)]
print(NQueen(c, b, n, 0, 0))