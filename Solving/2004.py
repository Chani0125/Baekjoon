n, k = map(int, input().split())
factor = 0
for i in range(k):
    up = n-i
    down = i+1
    while up % 10 == 0:
        factor += 1
        up //= 5
    while down % 10 == 0:
        factor -= 1
        down //= 5
if factor < 0:
    factor = 0
print(factor)
