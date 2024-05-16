n = int(input())
for i in range(1, 2*n):
    a = [' '] * abs(n-i) + ['*'] * ((n - abs(n-i)) * 2 - 1)
    print(*a, sep='')