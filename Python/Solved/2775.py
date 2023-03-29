t = int(input())
for r in range(t):
    k = int(input())
    n = int(input())

    apt = [list(range(1, n + 1))]
    for i in range(k):
        f = []
        for j in range(n):
            if j == 0:
                f.append(apt[i][j])
            else:
                f.append(apt[i][j] + f[j-1])
        apt.append(f)

    print(apt[k][n-1])