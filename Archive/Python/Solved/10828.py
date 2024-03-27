import sys


t = int(sys.stdin.readline())
stack = []
for _ in range(t):
    s = sys.stdin.readline().split()
    if s[0] == "push":
        stack.append(int(s[1]))
    elif s[0] == "pop":
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)
    elif s[0] == "size":
        print(len(stack))
    elif s[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif s[0] == "top":
        if len(stack) != 0:
            print(stack[len(stack)-1])
        else:
            print(-1)
