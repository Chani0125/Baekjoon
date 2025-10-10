import sys

x = int(sys.stdin.readline())
ans = 0

for i in range(8):
    if x & (1 << i):
        ans += 1

print(ans)