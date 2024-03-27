import sys

s = sys.stdin.readlines()[1:]
for i in s:
    print(f'{i[0]}{i[-2]}')