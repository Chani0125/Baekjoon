w, h = map(int, input().split())
x, y = map(int, input().split())

DIVIDER = 1000007

from math import comb

a = comb(x+y-2, y-1)
b = comb(w+h-x-y, h-y)
print((a * b) % DIVIDER)

