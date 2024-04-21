import sys

n = int(sys.stdin.readline())
nums = list(range(n, 0, -1))
goal_arr = [int(sys.stdin.readline()) for _ in range(n)]
stack = []
ans = []

make_arr = True

for _ in range(goal_arr[0]):
    stack.append(nums.pop())
    ans.append("+")
del stack[-1]
del goal_arr[0]
ans.append("-")

for i in goal_arr:
    if len(stack) == 0:
        ans.append("+")
        stack.append(nums.pop())
    while stack[-1] < i:
        ans.append("+")
        stack.append(nums.pop())
    if stack[-1] == i:
        del stack[-1]
        ans.append("-")
    else:
        make_arr = False
        break

if make_arr:
    print("\n".join(ans))
else:
    print("NO")