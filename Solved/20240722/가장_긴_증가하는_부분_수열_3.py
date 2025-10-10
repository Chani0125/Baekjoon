import sys, bisect

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

lis = []
for i in range(n):
    if i == 0 or arr[i] > lis[-1]:
        lis.append(arr[i])
    else:
        lis[bisect.bisect_left(lis, arr[i])] = arr[i]

print(len(lis))