import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline
n, r, q = map(int, input().split())
adj_list = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

v = [0] * (n+1)

def dfs(root):
    v[root] = 1
    for node in adj_list[root]:
        if v[node] == 0:
            dfs(node)
            v[root] += v[node]

dfs(r)

print(*[v[int(input())] for _ in range(q)], sep='\n')