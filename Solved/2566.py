a = [list(map(int, input().split())) for _ in range(9)]
x, y = 0, 0
max_ = a[0][0]
for i in range(9):
    for j in range(9):
        if a[i][j] > max_:
            max_ = a[i][j]
            x, y = i, j
print(max_)
print(x+1, y+1)