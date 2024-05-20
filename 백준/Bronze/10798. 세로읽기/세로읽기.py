import sys

input = sys.stdin.readline
a = [input().strip() for _ in range(5)]
for i in range(15):
    for j in range(5):
        if i < len(a[j]):
            print(a[j][i], end='')