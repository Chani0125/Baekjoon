k = int(input())
primes = [2]
n = 3

while len(primes) < k:
    for i in primes:
        if n % i == 0:
            break
    else:
        primes.append(n)
    n += 1

print(primes[-1])