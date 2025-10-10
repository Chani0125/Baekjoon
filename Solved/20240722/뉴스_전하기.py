import sys

input = sys.stdin.readline
n = int(input())
p = [*map(int, input().split())]

d = [0] * n
c = [[] for _ in range(n)]
for i in range(1, n):
    d[i] = d[p[i]] + 1
    c[p[i]].append(i)

r = [0] * n
def dfs(root):
    if len(c[root]) == 0:
        return 0
    
    a = []
    for node in c[root]:
        a.append(dfs(node))
    a.sort(reverse=True)
    
    b = [a[i]+i+1 for i in range(len(a))]
    return max(b)

print(dfs(0))
