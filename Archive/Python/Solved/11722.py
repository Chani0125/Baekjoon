import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().strip().split()))

min_arr = [1, ] * n

for i in range(1, n):
    for j in range(i):
        if arr[i] < arr[j]:
            if min_arr[i] < min_arr[j] + 1:
                min_arr[i] = min_arr[j] + 1

print(max(min_arr))
