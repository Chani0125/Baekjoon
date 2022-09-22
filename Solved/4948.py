def cal_prime_number(num):
    for i in range(1, int((2 * num) ** 0.5) + 1):
        if i == 1:
            continue
        elif i < 4:
            prime.append(i)
        else:
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    break
            else:
                prime.append(i)


n = int(input())
while not n == 0:
    c = 0
    prime = []
    cal_prime_number(n)
    for i in range(n+1, 2*n + 1):
        for j in prime:
            if i % j == 0:
                break
        else:
            c += 1

    print(c)
    n = int(input())
