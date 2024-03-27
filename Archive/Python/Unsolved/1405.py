def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def dfs(d, visit, n, depth, x, y):
    visit[x][y] = True
    if depth == n:
        return 1
    cnt = 0
    for i, dx, dy in [(0, 1, 0), (1, -1, 0), (2, 0, -1), (3, 0, 1)]:
        if not visit[x + dx][y + dy]:
            cnt += dfs(d, visit, n, depth+1, x + dx, y + dy) * d[i]
            visit[x + dx][y + dy] = False
    return cnt


d = [0 for _ in range(4)]
n, d[0], d[1], d[2], d[3] = map(int, input().split())
visit = [[False for _ in range(30)] for _ in range(30)]
gcds = d[0]
for i in d[1:]:
    gcds = gcd(gcds, i)
for i in range(4):
    d[i] //= gcds
ans = dfs(d, visit, n, 0, 15, 15) / sum(d) ** n
print(ans)