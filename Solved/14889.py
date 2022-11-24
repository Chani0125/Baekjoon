from itertools import combinations


n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(i+1, n):
        s[i][j] += s[j][i]

t = combinations(list(range(n)), n // 2)

ls = []
for team in t:
    total = 0
    for start in range(len(team) - 1):
        for end in range(start + 1, len(team)):
            total += s[team[start]][team[end]]
    another_team = tuple(set(range(n)) - set(team))
    another_total = 0
    for start in range(len(another_team) - 1):
        for end in range(start + 1, len(another_team)):
            another_total += s[another_team[start]][another_team[end]]
    ls.append(abs(total - another_total))

print(min(ls))
