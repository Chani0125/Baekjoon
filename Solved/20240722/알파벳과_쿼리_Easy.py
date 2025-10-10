import sys

input = sys.stdin.readline
n, q = map(int, input().split())
s = list(input().strip())

def alpha_group(l, r):
    cnt = 1
    for i in range(l, r):
        if s[i] != s[i-1]:
            cnt += 1
    return cnt

for _ in range(q):
    o, l, r = map(int, input().split())
    if o == 1:
        print(alpha_group(l, r))
    else:
        for i in range(l-1, r):
            s[i] = chr(ord(s[i]) + 1)
            if s[i] == '[': s[i] = 'A'


