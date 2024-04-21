N = int(input())
nums = [int(input()) for i in range(N)]

# Bubble Sort
for i in range(N):
    for j in range(N-i-1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]

for i in nums:
    print(i)
