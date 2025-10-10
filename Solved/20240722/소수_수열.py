n, k = map(int, input().split())

primes = []
for i in range(2, 1000000):
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        primes.append(i)

p = [i % k for i in primes]
q = [False] * len(primes)
a = []

for i in range(n):
    for idx, j in enumerate(p):
        if not q[idx] and j == 1:
            q[idx] = True
            a.append(primes[idx])
            break

print(*a)
