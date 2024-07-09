import sys
from collections import deque

d = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    l = int(input())
    curr = tuple(map(int, input().split()))
    dest = tuple(map(int, input().split()))
    
    stack = deque()
    stack.append((0, curr))
    visited = [[False] * l for _ in range(l)]
    
    while stack:
        n, (x, y) = stack.popleft()
        
        if visited[x][y]:
            continue
        visited[x][y] = True
        
        if (x, y) == dest:
            print(n)
            break
        
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                stack.append((n+1, (nx, ny)))
