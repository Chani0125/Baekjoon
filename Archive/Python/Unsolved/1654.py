k, n = map(int, input().split())
l = [int(input()) for _ in range(k)]
max_len = max(l)
for i in range(max_len, 0, -1):
    cnt = 0
    for j in l:
        cnt += j // i
    if cnt == n:
        print(i)
        break
