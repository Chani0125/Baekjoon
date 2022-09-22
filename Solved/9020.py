def find_prime_number(end):
    list_prime_idx = [False, False] + [True, ] * (end - 1)
    for i in range(2, end + 1):
        if i * i > end:
            break
        if not list_prime_idx[i]:
            continue
        for j in range(i * 2, end + 1, i):
            list_prime_idx[j] = False
    list_prime_num = []
    for idx, val in enumerate(list_prime_idx):
        if val:
            list_prime_num.append(idx)
    return list_prime_num


def decide_prime_number(num):
    if num == 1:
        return False
    elif num < 4:
        return True
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        else:
            return True


T = int(input())
for i in range(T):
    n = int(input())
    prime = find_prime_number(n//2)
    half = n // 2
    goldbach = []
    for j in prime[::-1]:
        if decide_prime_number(n - j):
            print(j, n - j)
            break

# def cal_prime_number(start, end):
#     prime = []
#     for i in range(start, end + 1):
#         if i < 4:
#             prime.append(i)
#         else:
#             for j in range(2, int(i ** 0.5) + 1):
#                 if i % j == 0:
#                     break
#             else:
#                 prime.append(i)
#     return prime
#
#
# def decide_prime_number(num):
#     if num == 1:
#         return False
#     elif num < 4:
#         return True
#     else:
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 return False
#         else:
#             return True
#
#
# T = int(input())
# for i in range(T):
#     n = int(input())
#     higher_prime = cal_prime_number(2, n // 2)
#     goldbach = []
#     for j in higher_prime[::-1]:
#         if decide_prime_number(n - j):
#             print(j, n - j)
#             break
