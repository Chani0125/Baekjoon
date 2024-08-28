from math import comb

def h(n, r):
    return comb(n+r-1, r)

DIV = 1000000007

n, m = map(int, input().split())

ans = 0
for idx, val in enumerate(range(n, -1, -m)):
    ans = (ans + h(idx+1, val)) % DIV
    
print(ans)