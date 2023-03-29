import sys


n, s = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
start = 0
end = 1
subtotal = a[0]
ans = len(a) + 1
while start < len(a):
    if subtotal >= s:
        if end - start < ans:
            ans = end - start
        subtotal -= a[start]
        start += 1
    elif end < len(a):
        subtotal += a[end]
        end += 1
    else:
        break
if subtotal >= s and end - start > ans:
    ans = end - start
if ans == len(a) + 1:
    ans = 0
print(ans)
