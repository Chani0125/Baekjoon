def factorization(num):
    for i in range(2, num+1):
        if num % i == 0:
            return i
    return 0


N = int(input())

while not N == 1:
    factor = factorization(N)
    print(factor)
    N //= factor
