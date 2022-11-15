def dfs(n, m, d, ans):
    if d == m:
        print(ans[1:])
        return
    for i in range(n):
        dfs(n, m, d + 1, ans + " " + str(i + 1))


n, m = map(int, input().split())
dfs(n, m, 0, "")
