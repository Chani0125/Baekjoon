import sys, bisect

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

lis = []
pos = [set() for _ in range(n)]
for i in range(n):
    if i == 0 or arr[i] > lis[-1]:
        idx = len(lis)
        lis.append(arr[i])
    else:
        idx = bisect.bisect_left(lis, arr[i])
        lis[idx] = arr[i]
    pos[i].add(idx)

now = len(lis)-1
res = []
for i in range(n):
    if now in pos[n-i-1]:
        res.insert(0, arr[n-i-1])
        now -= 1

print(len(lis))
print(*res)

