import sys
from collections import deque

# Input
n, q = map(int, sys.stdin.readline().strip().split())

graph = [list() for _ in range(n+1)]
for i in range(n):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

# Find Loop Element
graph_copy = [i.copy() for i in graph]
parent = [0, ] * (n+1)
exist_child = True
while exist_child:
    exist_child = False
    for i in range(len(graph_copy)):
        if len(graph_copy[i]) == 1:
            exist_child = True
            graph_copy[graph_copy[i][0]].remove(i)
            graph_copy[i] = []

visited = [False, ] * (n+1)

loop = set()
for i in graph_copy:
    if len(i) != 0:
        for j in i:
            loop.add(j)
            visited[j] = True

# Find Parent by DPS
stack_parent = deque(list(loop))
while stack_parent:
    parent_element = stack_parent.pop()
    parent[parent_element] = parent_element
    stack_child = deque()
    for element in graph[parent_element]:
        if not visited[element]:
            stack_child.append(element)
            visited[element] = True
    while stack_child:
        child_element = stack_child.pop()
        parent[child_element] = parent_element
        for element in graph[child_element]:
            if not visited[element]:
                stack_child.append(element)
                visited[element] = True

for _ in range(q):
    u, v = map(int, sys.stdin.readline().strip().split())
    if parent[u] == parent[v]:
        print(1)
    else:
        print(2)
