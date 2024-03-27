def factorization(num, m):
    for i in range(m, num+1):
        if num % i == 0:
            return i
    return 0


N = int(input())
factor = 2

while not N == 1:
    factor = factorization(N, factor)
    print(factor)
    N //= factor
