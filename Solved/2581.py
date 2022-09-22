M = int(input())
N = int(input())
prime = []

for i in range(M, N+1):
    if i == 1:
        continue
    elif i < 4:
        prime.append(i)
    else:
        for j in range(2, int(i**(1/2))+1):
            cal_prime = True
            if i % j == 0:
                cal_prime = False
                break
        if cal_prime:
            prime.append(i)

if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(min(prime))
