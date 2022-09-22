import sys

N = int(input())

# Counting Sort

# Finding max value
counting_array = []
for i in range(N):
    num = int(sys.stdin.readline())
    if len(counting_array) < num:
        counting_array += [0, ] * (num - len(counting_array))
    counting_array[num - 1] += 1

for idx, val in enumerate(counting_array):
    for j in range(val):
        print(idx+1)

# for i in range(1, len(counting_array)):
#     counting_array[i] += counting_array[i-1]
#
# # Make Output Array
# output_array = [None, ] * N
# for i in nums:
#     output_array[counting_array[i-1]-1] = i
#     counting_array[i - 1] -= 1
#
#
# for i in output_array:
#     print(i)
