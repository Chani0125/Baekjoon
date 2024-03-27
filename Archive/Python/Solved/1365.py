import sys
import bisect

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().strip().split()))

max_len = [0]
max_len_arr = [0]

for i in range(n):
    idx = bisect.bisect_left(max_len_arr, arr[i])

    if idx == len(max_len_arr):
        max_len.append(idx)
        max_len_arr.append(arr[i])
    else:
        max_len_arr[idx] = arr[i]

print(n - max_len[-1])
