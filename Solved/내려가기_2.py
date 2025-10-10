import sys

input = sys.stdin.readline
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

b = [[[0, ] * 3 for _ in range(3)] for _ in range(n)]
b[0][0] = [a[0][0], a[0][0], a[0][0]]
b[0][1] = [a[0][1], a[0][1], a[0][1]]
b[0][2] = [a[0][2], a[0][2], a[0][2]]

c = [[[1000000, ] * 3 for _ in range(3)] for _ in range(n)]
c[0][0] = [a[0][0], a[0][0], a[0][0]]
c[0][1] = [a[0][1], a[0][1], a[0][1]]
c[0][2] = [a[0][2], a[0][2], a[0][2]]

for i in range(1, n):
    b[i][0][0] = a[i][0] + max(b[i-1][0])
    b[i][0][1] = a[i][0] + max(b[i-1][1])
    
    b[i][1][0] = a[i][1] + max(b[i-1][0])
    b[i][1][1] = a[i][1] + max(b[i-1][1])
    b[i][1][2] = a[i][1] + max(b[i-1][2])
    
    b[i][2][1] = a[i][2] + max(b[i-1][1])
    b[i][2][2] = a[i][2] + max(b[i-1][2])
    
    c[i][0][0] = a[i][0] + min(c[i-1][0])
    c[i][0][1] = a[i][0] + min(c[i-1][1])
    
    c[i][1][0] = a[i][1] + min(c[i-1][0])
    c[i][1][1] = a[i][1] + min(c[i-1][1])
    c[i][1][2] = a[i][1] + min(c[i-1][2])
    
    c[i][2][1] = a[i][2] + min(c[i-1][1])
    c[i][2][2] = a[i][2] + min(c[i-1][2])
    
print(max(*b[-1][0], *b[-1][1], *b[-1][2]), min(*c[-1][0], *c[-1][1], *c[-1][2]))
