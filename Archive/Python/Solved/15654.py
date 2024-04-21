import sys


def combine(m, now, arr, s):
    if m == 1:
        print(s + str(arr[now]))
    else:
        for i in range(len(arr)):
            if not visited[i]:
                visited[i] = True
                combine(m - 1, i, arr, s + str(arr[now]) + " ")
                visited[i] = False


n, m = map(int, sys.stdin.readline().strip().split())
nums = sorted(list(map(int, sys.stdin.readline().strip().split())))

visited = [False, ] * n
for i in range(n):
    visited[i] = True
    combine(m, i, nums, "")
    visited[i] = False
