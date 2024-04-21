import sys
from collections import deque

n = int(sys.stdin.readline())
tree = [list() for _ in range(n+1)]
parent = [0 for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().strip().split())
    tree[a].append(b)
    tree[b].append(a)

queue = deque([1])
while queue:
    node = queue.popleft()
    for next_node in tree[node]:
        if parent[next_node] == 0:
            parent[next_node] = node
            queue.append(next_node)

print("\n".join(map(str, parent[2:n+1])))
