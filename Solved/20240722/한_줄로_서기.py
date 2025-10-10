import sys

input = sys.stdin.readline
n = int(input())
a = [*map(int, input().split())]
b = [0] * n

for i in range(n):
    cnt = 0
    for j in range(n):
        if b[j] == 0:
            if cnt == a[i]:
                b[j] = i+1
                break
            cnt += 1

print(*b, sep=' ')