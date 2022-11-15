def NQueen(b, n, depth):
    if depth == n:
        return 1
    cnt = 0
    for i in range(n):
        if not b[depth][i]:
            for j in range(depth+1, n):
                b[j][i] = True
                if i+j-depth < n:
                    b[j][i+j-depth] = True
                if i-j+depth >= 0:
                    b[j][i-j+depth] = True
            cnt += NQueen(b, n, depth+1)
            for j in range(depth+1, n):
                b[j][i] = False
                if i+j-depth < n:
                    b[j][i+j-depth] = False
                if i-j+depth >= 0:
                    b[j][i-j+depth] = False
    print(cnt)
    return cnt


n = int(input())
b = [[False for _ in range(n)] for _ in range(n)]
print(NQueen(b, n, 0))
