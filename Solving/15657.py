import sys


def combine(m, now, arr, s):
    if m == 1:
        print(s + str(arr[now]))
    else:
        for i in range(now, len(arr)):
            combine(m - 1, i, arr, s + str(arr[now]) + " ")


n, m = map(int, sys.stdin.readline().strip().split())
nums = sorted(list(map(int, sys.stdin.readline().strip().split())))

for i in range(n):
    combine(m, i, nums, "")