import sys
from bisect import bisect_left

input = sys.stdin.readline
n, q = map(int, input().split())
s = list(input().strip())

g_idx = [0]
g_chr = []

for i in range(1, n):
    if s[i] != s[i-1]:
        g_idx.append(i)
        g_chr.append(s[i-1])
g_idx.append(n)
g_chr.append(s[n-1])

def move(a):
    return chr(ord(a) + 1) if a != 'Z' else 'A'

for _ in range(q):
    o, l, r = map(int, input().split())
    if o == 1:
        print(len(g_idx)-1)
    else:
        left = bisect_left(g_idx, l-1)
        right = bisect_left(g_idx, r)
        if l-1 == g_idx[left] and left > 0:
            if g_chr[left-1] == move(g_chr[left]):
                del g_idx[left]
                del g_chr[left]
                right -= 1
        else:
            g_idx.insert(left, l-1)
            g_chr.insert(left, move(g_chr[left]))
        if r == g_idx[right] and right < len(g_idx)-1:
            if g_chr[right] == move(g_chr[right-1]):
                del g_idx[right]
                del g_chr[right]
        else:
            g_idx.insert(right, r)
            g_chr.insert(right, move(g_chr[right-1]))
        for i in range(left+1, right):
            g_chr[i] = move(g_chr[i])
