import sys
from collections import deque

t = int(sys.stdin.readline())
n, m = map(int, sys.stdin.readline().split())

adj_list = [[] for _ in range(n + 1)]
in_degrees = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    adj_list[a].append(b)
    in_degrees[b] += 1

# for idx, i in enumerate(adj_list):
#     print(f'{idx}:', end=' ')
#     for j in i:
#         print(j, end=' ')
#     print()

