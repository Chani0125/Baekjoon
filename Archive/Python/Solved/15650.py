def dfs(s, n, m, d, ans):
    if d == m:
        print(ans[1:])
        return
    for i in range(s, n):
        if not visit[i]:
            visit[i] = True
            dfs(i + 1, n, m, d + 1, ans + " " + str(i + 1))
            visit[i] = False


n, m = map(int, input().split())
visit = [False for _ in range(n)]
dfs(0, n, m, 0, "")
