import sys


def merge_sort_index(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (high + low) // 2
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

    sort(0, len(arr))
    return arr

N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for i in range(N)]
merge_sort_index(nums)
for i in nums:
    print(i)
