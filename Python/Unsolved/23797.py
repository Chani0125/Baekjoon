word = list(input())
now = word[0]
count = 1


# num = []
# for i in word[1::]:
#     if i == now:
#         count += 1
#     else:
#         num.append(count)
#         count = 1
#         now = i
# num.append(count)
# print(num)
#
# frog = num[0]
# a = frog
# c = -1
# for i in num[1::]:
#     a += i * c
#     if a < 0:
#         print(frog)
#         frog = num[0] - a
#         a = 0
#     c *= -1
# print(frog)


# num = []
# for i in word[1::]:
#     if i == now:
#         count += 1
#     else:
#         num.append(count)
#         count = 1
#         now = i
# num.append(count)

# a = [num[0], num[1]]
# for idx, val in enumerate(num[2::]):
#     if idx % 2 == 0:
#         if a[0] < val:
#             a[0] = val
#         if a[1] < val:
#             a[0] += val - a[1]
#         print(a)
#     else:
#         if a[1] < val:
#             a[1] = val
#         if a[0] < val:
#             a[1] += val - a[0]
#         print(a)
#
# print(max(a))

# frog = 0
# c = 0
# num = [[], []]
# for i in word[1::]:
#     if i == now:
#         count += 1
#     else:
#         num[c].append(count)
#         count = 1
#         now = i
#         c = 1 - c
# num[c].append(count)
#
# while len(num[0]) > 0 and len(num[1]) > 0:
#     min_ = min(min(num[0], num[1]))
#     if min_ == 0:
#         for i in range(2):
#             while num[i][-1] == 0:
#                 del num[i][-1]
#                 if len(num[i]) == 0:
#                     break
#         for i in range(2):
#             if len(num[i]) == 0:
#                 break
#             while min(num[i]) == 0:
#                 idx = num[i].index(0)
#                 try:
#                     num[1-i][idx] += num[1-i][idx+1]
#                 except:
#                     pass
#                 try:
#                     del num[1-i][idx+1]
#                 except:
#                     pass
#                 del num[i][idx]
#     else:
#         for i in range(2):
#             for j in range(len(num[i])):
#                 num[i][j] -= min_
#         frog += min_
# for i in range(2):
#     if len(num[i]) > 0:
#         frog += num[i][0]
# print(frog)


# KKKPKKPKKKPPK - 6
# KKKPKPKKKPPKPPPPKK
