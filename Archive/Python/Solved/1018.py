N, M = map(int, input().split())
board = []
color = ("W", "B")
nums = []

for i in range(N):
    board.append(list(input()))

for i in range(N-7):
    for j in range(M-7):
        for a in range(2):
            # code = color.index(board[i][j])
            code = a
            num = 0
            for k in range(8):
                for l in range(8):
                    if not board[i+k][j+l] == color[code]:
                        num += 1
                    code = 1 - code
                code = 1 - code
            nums.append(num)

print(min(nums))
