import sys

def ccw(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

n = int(sys.stdin.readline())
dots = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
base = dots[0]

ans = 0
for i in range(1, n-1):
    ans += ccw(dots[0], dots[i], dots[i+1])
print(abs(ans)/2)