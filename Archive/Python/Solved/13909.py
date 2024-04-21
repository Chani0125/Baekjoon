# import time


print(int(int(input()) ** 0.5))

# def check_window(num):
#     d = 2
#     prime_factor = {}
#     while True:
#         tmp = True
#         for i in range(d, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 num //= i
#                 if i in prime_factor:
#                     prime_factor[i] += 1
#                 else:
#                     prime_factor[i] = 1
#                 if not i == d and not d == 2:
#                     if prime_factor[d] % 2 == 1:
#                         return 0
#                 d = i
#                 tmp = False
#                 break
#         if tmp:
#             if num in prime_factor:
#                 prime_factor[num] += 1
#             else:
#                 prime_factor[num] = 1
#             break
#     num_divisor = 1
#     for j in prime_factor.values():
#         num_divisor *= j + 1
#     return num_divisor % 2
#
#
# n = int(input())
# first_time = time.time()
#
# # print(check_window(n))
#
# num_window = 1
# for i in range(2, n+1):
#     num_window += check_window(i)
# print(num_window)
#
# print(f"It takes {time.time()-first_time}s")


# import time
#
#
# def count_window(end):
#     windows = [1, ] * end
#     for i in range(1, end + 1):
#         for j in range(i, end + 1, i + 1):
#             try:
#                 windows[j] = 1 - windows[j]
#             except IndexError:
#                 continue
#     return windows.count(1)
#
#
# n = int(input())
# first_time = time.time()
# print(count_window(n))
# print(f"It takes {time.time()-first_time}s")
