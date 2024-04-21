import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
k = max(a) + 1

parent = [-1, ] * k
visited = [False, ] * k
visited[a[0]] = True

for i in range(1, len(a)):
    if not visited[a[i]]:
        parent[a[i]] = a[i-1]
    visited[a[i]] = True

print(k)
print(" ".join(map(str, parent)))
