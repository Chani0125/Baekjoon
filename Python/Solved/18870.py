import sys


N = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))

nums = {}
now = None
cnt = 0
for i in sorted(X):
    if not i == now:
        now = i
        nums[i] = cnt
        cnt += 1
for i in X:
    print(nums[i], end=" ")
