import sys
from math import ceil

input = sys.stdin.readline
n = int(input())
memo = {0, 1, 2}

def func(x):
    if x < 3 or x in memo: return
    
    a = ceil(x ** 0.5)
    if a ** 2 < x:
        a += 1
    b = a ** 2 - x
    
    func(a)
    memo.add(a)
    func(b)
    memo.add(b)
    
    print(a, b)

if n < 3:
    print(1, 1)
func(n)