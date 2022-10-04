# Use Splice
def merge_sort_slice(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort_slice(arr[:mid])
    high_arr = merge_sort_slice(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr


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


lst = [19, 1, 17, 3, 20, 15, 5, 13, 7, 11, 9, 18, 2, 16, 4, 14, 6, 0, 12, 8, 10]
print(merge_sort_slice(lst))
print(merge_sort_index(lst))
