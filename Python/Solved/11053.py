import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().strip().split()))

max_arr = [1, ] * n

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            if max_arr[i] < max_arr[j] + 1:
                max_arr[i] = max_arr[j] + 1

print(max(max_arr))
