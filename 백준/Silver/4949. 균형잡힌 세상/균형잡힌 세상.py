import sys
from collections import deque

strs = sys.stdin.readlines()

for s in strs[:-1]:
    dq = deque()
    for c in s:
        if c == '(':
            dq.append(0)
        elif c == ')':
            if not dq or dq.pop() != 0:
                break
        elif c == '[':
            dq.append(1)
        elif c == ']':
            if not dq or dq.pop() != 1:
                break
    else:
        if not dq and s[-2] == '.':
            print('yes')
            continue
    print('no')