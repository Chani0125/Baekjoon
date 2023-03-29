import sys

n = int(sys.stdin.readline())

list_prime_idx = [False, False] + [True, ] * (n - 1)
for i in range(2, n + 1):
    if i * i > n:
        break
    if not list_prime_idx[i]:
        continue
    for j in range(i * 2, n + 1, i):
        list_prime_idx[j] = False
list_prime_num = []
for idx, val in enumerate(list_prime_idx):
    if val:
        list_prime_num.append(idx)

if n == 1:
    print(0)
else:
    start = 0
    end = 1
    now_sum = list_prime_num[0]
    ans = 0

    while start < len(list_prime_num):
        if now_sum >= n:
            if now_sum == n:
                ans += 1
            now_sum -= list_prime_num[start]
            start += 1
        else:
            if end == len(list_prime_num):
                break
            now_sum += list_prime_num[end]
            end += 1

    print(ans)
