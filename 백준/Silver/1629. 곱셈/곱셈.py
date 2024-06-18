import sys

sys.setrecursionlimit(1000000)

a, b, c = map(int, sys.stdin.readline().split())

def my_pow(n, e):
    if e == 1: return n
    p = my_pow(n, e//2) % c
    ans = p * p
    if e % 2: ans *= n
    return ans % c

print(my_pow(a, b) % c)