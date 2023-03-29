def cal_prime_number(num):
    if num == 1:
        return 0
    elif num < 4:
        return 1
    else:
        for i in range(2, int(num**(1/2))+1):
            if num % i == 0:
                return 0
        return 1


n = int(input())
n_list = list(map(int, input().split()))
total = 0
for i in n_list:
    total += cal_prime_number(i)
print(total)
