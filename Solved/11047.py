import sys

n, k = map(int, sys.stdin.readline().strip().split())
a = [int(sys.stdin.readline()) for _ in range(n)]

cnt = 0

for value in a[::-1]:
    now, k = divmod(k, value)
    cnt += now

print(cnt)
