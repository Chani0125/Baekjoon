import sys
input = sys.stdin.readline
n = int(input())
dic = {}
now = 10000
for _ in range(n):
    a, b, c = map(int, input().split())
    if a in dic:
        if dic[a] < 0 and dic[a] < dic[a] + b * c:
            now = a
        elif dic[a] > 0 and dic[a] > dic[a] + b * c:
            now = a
        elif dic[a] == 0:
            now = a
        dic[a] = dic[a] + b * c
    else:
        dic[a] = b * c

print(now)