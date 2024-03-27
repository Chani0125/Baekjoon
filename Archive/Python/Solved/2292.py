n = int(input())
if n == 1:
    print(1)
else:
    m = 1
    while 6 * (1+m) * m / 2 < n-1:
        m += 1
    print(m+1)
