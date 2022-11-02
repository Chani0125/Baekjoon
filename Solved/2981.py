import sys


def gcd(a, b):
    while not b == 0:
        r = a % b
        a = b
        b = r
    return a


n = int(sys.stdin.readline())
nums = sorted([int(sys.stdin.readline()) for i in range(n)])
m = set()
if len(nums) == 2:
    d = nums[1] - nums[0]
    for i in range(2, int(d**0.5) + 1):
        if d % i == 0:
            m.add(i)
            m.add(d // i)
    if not d == 1:
        m.add(d)
else:
    n_gcd = gcd(nums[1] - nums[0], nums[2] - nums[1])
    for i in range(3, len(nums)):
        n_gcd = gcd(n_gcd, nums[i] - nums[i-1])
    for i in range(2, int(n_gcd**0.5) + 1):
        if n_gcd % i == 0:
            m.add(i)
            m.add(n_gcd // i)
    if not n_gcd == 1:
        m.add(n_gcd)
print(" ".join(map(str, sorted(m))))

