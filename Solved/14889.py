def synergy(n, s, t, ls):
    for team in t:
        total = 0
        for start in range(len(team)-1):
            for end in range(start+1, len(team)):
                total += s[team[start]][team[end]]
        another_team = tuple(set(range(n)) - set(team))
        another_total = 0
        for start in range(len(another_team)-1):
            for end in range(start+1, len(another_team)):
                another_total += s[another_team[start]][another_team[end]]
        ls.append(abs(total-another_total))


def makeTeam(n, t, st, m):
    if len(m) == n // 2:
        return True
    for i in range(st+1, n//2 + len(m) + 1):
        m.append(i)
        if makeTeam(n, t, i, m):
            t.append(tuple(m))
        m.pop()
    return False


n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
t = []
ls = []
for i in range(n):
    for j in range(i+1, n):
        s[i][j] += s[j][i]
for i in range(n // 2 + 1):
    m = [i, ]
    makeTeam(n, t, i, m)
synergy(n, s, t, ls)
print(min(ls))