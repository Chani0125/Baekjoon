import sys, bisect

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

lis = []
pos = [0] * n
lis.append(arr[0])
for i in range(1, n):
    if arr[i] > lis[-1]:
        idx = len(lis)
        lis.append(arr[i])
    else:
        idx = bisect.bisect_left(lis, arr[i])
        lis[idx] = arr[i]
    pos[i] = idx

print(len(lis))
now = n-1
res = []
for i in range(len(lis)-1, -1, -1):
    while pos[now] != i: now -= 1
    res.append(arr[now])
    
print(*res[::-1])