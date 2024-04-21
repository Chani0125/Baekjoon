def dfs(n, m, d, ans):
    if d == m:
        print(ans[1:])
        return
    for i in range(n):
        if not visit[i]:
            visit[i] = True
            dfs(n, m, d + 1, ans + " " + str(i + 1))
            visit[i] = False


n, m = map(int, input().split())
visit = [False for _ in range(n)]
dfs(n, m, 0, "")
