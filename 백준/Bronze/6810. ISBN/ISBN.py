a = list(map(int, list('9780921418'))) + [int(input()) for _ in range(3)]
b = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1]

ans = 0
for i in range(13):
    ans += a[i] * b[i]
print(f'The 1-3-sum is {ans}')