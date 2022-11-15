def dfs(s, n, m, d, ans):
    if d == m:
        print(ans[1:])
        return
    for i in range(s, n):
        dfs(i, n, m, d + 1, ans + " " + str(i + 1))


n, m = map(int, input().split())
dfs(0, n, m, 0, "")
