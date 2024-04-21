import sys

N = int(sys.stdin.readline())
nums = sorted([int(sys.stdin.readline()) for i in range(N)])

fre = {}
max_fre = 1
for i in nums:
    if i in fre:
        fre[i] += 1
        if fre[i] > max_fre:
            max_fre = fre[i]
    else:
        fre[i] = 1
n_fre = []
for n, f in fre.items():
    if f == max_fre:
        n_fre.append(n)
n_fre.sort()

print(round(sum(nums) / N))
print(nums[N // 2])
if len(n_fre) > 1:
    print(n_fre[1])
else:
    print(n_fre[0])
print(nums[-1] - nums[0])
