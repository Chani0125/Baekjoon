import sys

input = sys.stdin.readline
n = float(input())

while n != 0:
    
    if n == 1:
        a = 5
    else:
        a = (n**5 - 1) /  (n - 1)
    print(f'{a:.2f}')
    
    n = float(input())