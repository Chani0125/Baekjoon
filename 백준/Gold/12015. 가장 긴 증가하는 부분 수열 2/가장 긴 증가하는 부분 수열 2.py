import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().strip().split()))

max_len = [0]
max_len_arr = [0]

for i in range(n):
    # Binary Search
    goal = arr[i]
    start = 0
    end = len(max_len_arr)
    while start + 1 != end:
        mid = (start + end) // 2
        if max_len_arr[mid] == goal:
            idx = mid
            break
        elif max_len_arr[mid] > goal:
            end = mid
        else:
            start = mid
    else:
        if max_len_arr[start] >= goal:
            idx = start
        else:
            idx = end
    
    if idx == len(max_len_arr):
        max_len.append(idx)
        max_len_arr.append(arr[i])
    else:
        max_len_arr[idx] = arr[i]

print(max_len[-1])
