import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

if len(nums) == 2 and nums[0] == nums[1]:
    print(nums[0])
elif len(nums) < 3:
    print("A")
else:
    p = nums[0] - nums[1]
    q = nums[1] - nums[2]
    if p == 0:
        if q == 0:
            if min(nums) == max(nums):
                print(nums[-1])
            else:
                print("B")
        else:
            print("B")
    elif q % p == 0:
        a = q // p
        b = nums[1] - nums[0] * a
        for i in range(3, len(nums)):
            if nums[i] != nums[i-1] * a + b:
                print("B")
                break
        else:
            print(nums[-1] * a + b)
    else:
        print("B")

