def NQueen(t, b, n, depth):
    if depth == n:
        return 1
    cnt = 0
    for i in range(n):
        if not b[depth][i]:
            tmp = []
            for j in range(depth+1, n):
                if not b[j][i]:
                    b[j][i] = True
                    tmp.append((j, i))
                if i+j-depth < n:
                    if not b[j][i+j-depth]:
                        b[j][i+j-depth] = True
                        tmp.append((j, i+j-depth))
                if i-j+depth >= 0:
                    if not b[j][i-j+depth]:
                        b[j][i-j+depth] = True
                        tmp.append((j, i-j+depth))
                t[depth] = tmp[:]
            cnt += NQueen(t, b, n, depth+1)
            for p, q in t[depth]:
                b[p][q] = False
    return cnt


n = int(input())
b = [[False for _ in range(n)] for _ in range(n)]
t = [[] for _ in range(n)]
print(NQueen(t, b, n, 0))