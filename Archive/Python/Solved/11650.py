n = int(input())
nums = []
for i in range(n):
    x, y = map(int, input().split())
    nums.append((x, y))
nums.sort(key=lambda k: (k[0], k[1]))
for x, y in nums:
    print(x, y)