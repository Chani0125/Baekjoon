def hansu(num):
    n_list = list(map(int, list(str(num))))
    if len(n_list) < 3:
        return 1
    else:
        d = n_list[1] - n_list[0]
        ans = 1
        for i in range(2, len(n_list)):
            if not n_list[i] - n_list[i-1] == d:
                ans = 0
        return ans


n = int(input())
count = 0
for i in range(1, n+1):
    count += hansu(i)
print(count)