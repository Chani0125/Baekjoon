import sys

n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

start = 2 ** 0
end = 2 ** 31
cur = 30

cut_len = 2 ** 30
cut_sum = 0
while cur > 0:
    cut_sum = 0
    for length_tree in trees:
        if length_tree > cut_len:
            cut_sum += length_tree - cut_len
            if cut_sum > m:
                start = cut_len + 1
                cur -= 1
                cut_len = cut_len + 2 ** cur
                # print(cut_len, start, end, cut_sum, cur, 0)
                break
    else:
        # print(cut_len, start, end, cut_sum, cur, 1)
        if cut_sum == m:
            print(cut_len)
            break
        elif cut_sum > m:
            start = cut_len + 1
            cur -= 1
            cut_len = cut_len + 2 ** cur
        else:
            end = cut_len - 1
            cur -= 1
            cut_len = cut_len - 2 ** cur

else:
    cut_sum = 0
    for length_tree in trees:
        if length_tree > cut_len:
            cut_sum += length_tree - cut_len
    # print(cut_len, start, end, cut_sum, cur, 2)
    if cut_sum >= m:
        print(cut_len)
    else:
        print(cut_len-1)
