def facto(n):
    if n == 1 or n == 0:
        return 1
    return n * facto(n-1)


num = facto(int(input()))
ans = 0
while num % 10 == 0:
    ans += 1
    num //= 10
print(ans)
