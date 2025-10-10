n = int(input())
a = list(map(int, input().split()))

def cost(p):
    ret = 0
    for i in range(n):
        ret = max(ret, abs(i-p) * a[i])
    return ret

lo, hi = 0, n-1
while hi - lo >= 3:
    p = (lo*2 + hi) // 3
    q = (lo + hi*2) // 3
    if cost(p) > cost(q):
        lo = p
    else:
        hi = q

print(min(map(cost, range(lo, hi+1))))