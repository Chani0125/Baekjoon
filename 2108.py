N = int(input())
nums = sorted([int(input()) for i in range(N)])

fre = {}
for i in nums:
    if i in fre:
        fre[i] += 1
    else:
        fre[i] = 1

print(round(sum(nums) / N))
print(nums[N // 2])
print(fre)
print(max(nums) - min(nums))
