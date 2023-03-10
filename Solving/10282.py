import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    n, d, c = map(int, sys.stdin.readline().split())
    computers = [tuple(map(int, sys.stdin.readline().split())) for _ in range(d)]

    infections = [False, ] * n
    # depend = [[0, ] * n for _ in range(n)]
    # for a, b, s in computers:
    #     depend[b-1][a-1] = s

    total_time = 0

    infections[c - 1] = True
    current = deque([(co[0]-1, co[2]) for co in computers if co[1] == c])

    while len(current) > 0:
        min_time = min([i[1] for i in current])
        total_time += min_time
        # print(current, min_time)
        for i in range(len(current)):
            if len(current) > 0:
                comp, time = current.popleft()
                if time == min_time:
                    infections[comp] = True
                    # print(0, current)
                    for co in computers:
                        if co[1]-1 == comp and not infections[co[0]-1]:
                            current.append((co[0]-1, co[2]))
                            # print(1, current)
                else:
                    current.append((comp, time - min_time))
        current = deque([(i[0], i[1]) for i in current if not infections[i[0]]])

    print(infections.count(True), total_time)

    # print("\n".join(map(str, depend)))
    # print(infections, total_time)
