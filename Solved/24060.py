import math


def merge_sort_index(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = math.ceil((high + low) / 2)
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1

        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]
            save_arr.append(arr[i])

    sort(0, len(arr))


A, K = map(int, input().split())
N = list(map(int, input().split()))
save_arr = []
merge_sort_index(N)
if K < len(save_arr):
    print(save_arr[K-1])
else:
    print(-1)