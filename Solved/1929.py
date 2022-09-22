M, N = map(int, input().split())
prime = []

for i in range(M, N+1):
    if i == 1:
        continue
    elif i < 4:
        prime.append(i)
    else:
        for j in range(2, int(i**(1/2))+1):
            if i % j == 0:
                break
        else:
            prime.append(i)

for i in prime:
    print(i)
