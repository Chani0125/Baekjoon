n = int(input())
s = [[False for _ in range(100)] for _ in range(100)]
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            s[i][j] = True
cnt = 0
for i in s:
    for j in i:
        if j:
            cnt += 1
print(cnt)
