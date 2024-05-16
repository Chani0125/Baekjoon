import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())
num = [int(input()) for _ in range(n)]

seg_tree = [1] * (n << 2)

def segment(l, r, i):
    if l == r:
        seg_tree[i] = num[l-1]
        return seg_tree[i]
    mid = (l + r) // 2
    seg_tree[i] = segment(l, mid, i << 1) * segment(mid + 1, r, i << 1 | 1) % 1000000007
    return seg_tree[i]

def search(s, e, l, r, i):
    if e < l or r < s: return 1
    if l <= s and e <= r: return seg_tree[i]
    mid = (s + e) // 2
    return search(s, mid, l, r, i << 1) * search(mid + 1, e, l, r, i << 1 | 1) % 1000000007

def update(s, e, idx, val, i):
    if idx < s or e < idx: return seg_tree[i]
    if s == e:
        seg_tree[i] = val
        return seg_tree[i]
    mid = (s + e) // 2
    seg_tree[i] = update(s, mid, idx, val, i << 1) * update(mid + 1, e, idx, val, i << 1 | 1) % 1000000007
    return seg_tree[i]
    
segment(1, n, 1)
for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(1, n, b, c, 1)
    else:
        print(search(1, n, b, c, 1) % 1000000007)
