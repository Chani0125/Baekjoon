import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

for i in range(b[0]):
    b[i+1] = b[i+1] - (n//3)
    if b[i+1] < 1:
        b[i+1] += n
for i in range(c[0]):
    c[i+1] = c[i+1] - (n//3 * 2)
    if c[i+1] < 1:
        c[i+1] += n

# print(a, b, c, sep='\n', end='\n\n')

INF = 10**9
dp = [[[(INF, 0) for _ in range(c[0]+1)] for _ in range(b[0]+1)] for _ in range(a[0]+1)]

def dist(from_, to_):
    if from_ == to_: return 0
    r = from_ - to_
    l = to_ - from_
    if r < 0: r += n
    if l < 0: l += n
    
    return min(r, l)


dp[0][0][0] = (0, 1)

from itertools import combinations_with_replacement

sets = [0, 1, 2]
for t in range(1, a[0]+b[0]+c[0] + 1):
    hs = list(combinations_with_replacement(sets, t))
    for h in hs:
        i, j, k = h.count(0), h.count(1), h.count(2)
        if i > a[0] or j > b[0] or k > c[0]: continue
        
        min_ = INF
        from_ = dp[i][j][k][1]
        
        if i > 0 and min_ >= dp[i-1][j][k][0] + dist(dp[i-1][j][k][1], a[i]):
            min_ = dp[i-1][j][k][0] + dist(dp[i-1][j][k][1], a[i])
            from_ = a[i]
        if j > 0 and min_ >= dp[i][j-1][k][0] + dist(dp[i][j-1][k][1], b[j]):
            min_ = dp[i][j-1][k][0] + dist(dp[i][j-1][k][1], b[j])
            from_ = b[j]
        if k > 0 and min_ >= dp[i][j][k-1][0] + dist(dp[i][j][k-1][1], c[k]):
            min_ = dp[i][j][k-1][0] + dist(dp[i][j][k-1][1], c[k])
            from_ = c[k]
            
        dp[i][j][k] = (min_, from_) 

for d in dp:
    print(*d, sep='\n', end='\n\n')

print(dp[a[0]][b[0]][c[0]][0])

# [3, 7, 1]
# [8, 1, 7, 8]
# [3, 8, 9, 8]

# [[0, 1], [2, 3], [6, 8], [7, 9], [8, 8]]
# [[2, 8], [6, 8], [6, 8], [7, 9], [8, 8]]
# [[4, 1], [6, 3], [8, 1], [8, 1], [10, 1]]
# [[7, 7], [10, 7], [11, 7], [11, 7], [12, 8]]
# [[8, 8], [11, 8], [11, 8], [12, 8], [12, 8]]

# [[2, 3], [2, 3], [6, 8], [7, 9], [8, 8]]
# [[6, 3], [6, 8], [6, 8], [7, 9], [8, 8]]
# [[6, 3], [6, 3], [8, 1], [8, 1], [10, 1]]
# [[10, 7], [10, 7], [11, 7], [11, 7], [12, 8]]
# [[11, 8], [11, 8], [11, 8], [12, 8], [12, 8]]

# [[6, 7], [6, 7], [7, 7], [9, 7], [9, 7]]
# [[7, 8], [7, 7], [7, 7], [9, 7], [9, 7]]
# [[9, 1], [10, 7], [10, 1], [11, 7], [12, 1]]
# [[10, 7], [10, 7], [11, 7], [11, 7], [12, 8]]
# [[11, 8], [11, 8], [11, 8], [12, 8], [12, 8]]

# [[9, 1], [9, 1], [10, 1], [11, 9], [12, 1]]
# [[9, 1], [10, 1], [10, 1], [11, 9], [12, 1]]
# [[9, 1], [10, 1], [10, 1], [11, 9], [12, 1]]
# [[12, 7], [13, 1], [13, 7], [13, 7], [14, 1]]
# [[13, 1], [13, 1], [13, 1], [14, 1], [14, 1]]

# 14