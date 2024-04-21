import sys
from collections import deque


n = int(sys.stdin.readline())
cost = [0, ] * (n + 1)
cost[1] = 0

cnt = 0
queue = deque([1])
# print(queue, cost)

while queue or cnt == 3:
    now = queue.popleft()
    for i in [3, 2]:
        if now * i <= n:
            if cost[now * i] > cost[now] + 1 or cost[now * i] == 0:
                cost[now * i] = cost[now] + 1
                if now * i == n:
                    cnt += 1
                else:
                    queue.appendleft(now * i)
    if now + 1 <= n:
        if cost[now + 1] > cost[now] + 1 or cost[now + 1] == 0:
            cost[now + 1] = cost[now] + 1
            if now + 1 == n:
                cnt += 1
            else:
                queue.append(now + 1)
    # print(queue, cost)

print(cost[n])
