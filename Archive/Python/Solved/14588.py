import sys


def Floyd_Warshall(N, d):
    for m in range(N):
        for s in range(N):
            for e in range(N):
                if d[s][e] > d[s][m] + d[m][e]:
                    d[s][e] = d[s][m] + d[m][e]


N = int(sys.stdin.readline())
lines = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
Q = int(sys.stdin.readline())
line_question_nums = [tuple(map(int, sys.stdin.readline().split())) for _ in range(Q)]
d = [[N+1 for _ in range(N)] for _ in range(N)]

line_links = [list() for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            d[i][j] = 0
        elif lines[i][0] <= lines[j][0] <= lines[i][1]:
            d[i][j] = 1
            line_links[i].append(j)
        elif lines[i][0] <= lines[j][1] <= lines[i][1]:
            d[i][j] = 1
            line_links[i].append(j)
        elif lines[j][0] <= lines[i][0] <= lines[j][1]:
            d[i][j] = 1
            line_links[i].append(j)

Floyd_Warshall(N, d)

for a, b in line_question_nums:
    ans = d[a-1][b-1]
    if ans > N:
        print(-1)
    else:
        print(ans)
