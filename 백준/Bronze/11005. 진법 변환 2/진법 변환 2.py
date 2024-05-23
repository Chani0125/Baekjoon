n, b = map(int, input().split())

s = ''
while n > 0:
    if n % b < 10:
        s = str(n % b) + s
    else:
        s = chr(n % b + 55) + s
    n //= b
print(s)