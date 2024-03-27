n, m = map(int, input().split())
n = abs(n)
m = abs(m)
if n == 0 and m == 0:
    print(0)
elif n == 1 or m == 1:
    print(1)
elif n == 0 or m == 0:
    print(2)
else:
    if n > m:
        a = n
        b = m
    else:
        a = m
        b = n
    while not b == 0:
        r = a % b
        a = b
        b = r
    if a == 1:
        print(1)
    else:
        print(2)