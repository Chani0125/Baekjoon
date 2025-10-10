import sys

input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0

def dfs(idx, sum):
    global cnt
    
    if idx >= n: return
    if sum + arr[idx] == s: cnt += 1
    
    dfs(idx + 1, sum)
    dfs(idx + 1, sum + arr[idx])

dfs(0, 0)

print(cnt)
