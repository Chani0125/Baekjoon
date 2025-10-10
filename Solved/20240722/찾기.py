import sys

input = sys.stdin.readline
a = list(input().strip('\n'))
b = list(input().strip('\n'))

dp = [0] * len(b)
for i in range(1, len(b)):
    # print(dp)
    j = dp[i-1]
    while j > 0 and b[i] != b[j]:
        j = dp[j-1]
    if b[i] == b[j]:
        j += 1
    dp[i] = j

ans = []
j = 0
for i in range(len(a)):
    while j > 0 and a[i] != b[j]:
        j = dp[j-1]
    if a[i] == b[j]:
        if j == len(b)-1:
            ans.append(i-len(b)+2)
            j = dp[j]
        else:
            j += 1

print(len(ans))
print(*ans)
