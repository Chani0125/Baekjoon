import sys

input = sys.stdin.readline
n = int(input())
a = [1000000001] + [*map(int, input().split())]
m = int(input())

class SegmentTree:
    def segment(self, s, e, idx=1):
        if s == e:
            self.tree[idx] = s
            return self.tree[idx]
        
        m = (s + e) // 2
        a = self.segment(s, m, idx*2)
        b = self.segment(m+1, e, idx*2+1)

        if self.arr[a] <= self.arr[b]:
            self.tree[idx] = a
        else:
            self.tree[idx] = b
            
        return self.tree[idx]
    
    def search(self, s, e, l, r, idx=1):
        if e < l or r < s: return 0
        if l <= s and e <= r: return self.tree[idx]
        m = (s + e) // 2
        
        a = self.search(s, m, l, r, idx*2)
        b = self.search(m+1, e, l, r, idx*2+1)
        
        if self.arr[a] <= self.arr[b]:
            return a
        return b
                
    def update(self, s, e, arr_idx, diff, idx=1):
        if arr_idx < s or e < arr_idx: return
        
        if s == e: return
        
        m = (s + e) // 2
        self.update(s, m, arr_idx, diff, idx*2)
        self.update(m+1, e, arr_idx, diff, idx*2+1)

        a = self.tree[idx*2]
        b = self.tree[idx*2+1]
        
        if self.arr[a] <= self.arr[b]:
            self.tree[idx] = a
        else:
            self.tree[idx] = b
        
    def __init__(self, arr):
        self.arr = arr
        self.height = len(arr).bit_length()
        self.tree = [0] * (2 << self.height)
        self.segment(0, len(arr) - 1)


seg_tree = SegmentTree(a)
for _ in range(m):
    p, q, r = map(int, input().split())
    
    if p == 1:
        seg_tree.arr[q] = r
        seg_tree.update(0, len(a)-1, q, r)
    else:
        idx = seg_tree.search(0, len(a)-1, q, r)
        print(idx)
