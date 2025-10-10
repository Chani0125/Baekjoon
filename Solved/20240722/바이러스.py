import sys

input = sys.stdin.readline
v = int(input())
e = int(input())

parent = [*range(v)]
rank = [0] * v

def find(x):
    if parent[x] == x: return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x, y = find(x), find(y)
    if x == y: return
    if rank[x] > rank[y]:
        parent[y] = x
    elif rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[x] = y
        rank[y] += 1
        
for _ in range(e):
    a, b = map(int, input().split())
    union(a-1, b-1)

n = find(0)
ans = sum([int(find(i) == n) for i in range(v)])
print(ans-1)