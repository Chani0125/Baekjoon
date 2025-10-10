import sys

input = sys.stdin.readline
n, b = input().split()
b = int(b)

ans = 0
for i in range(len(n)):
    if 65 <= ord(n[-i-1]) <= 90:
        ans += (ord(n[-i-1]) - 55) * (b ** i)
    else:
        ans += int(n[-i-1]) * (b ** i)
print(ans)