import sys
from math import ceil, log

input = sys.stdin.readline
n, m, k = map(int, input().split())
num = [int(input()) for _ in range(n)]

class SegmentTree:
    def segment(self, left, right, i=1):
        if left == right:
            self.tree[i] = self.arr[left]
            return self.tree[i]
        mid = (left + right) // 2
        self.tree[i] = self.segment(left, mid, i*2) + self.segment(mid+1, right, i*2 + 1)
        return self.tree[i]
    
    def search(self, start, end, left, right, i=1):
        if end < left or right < start: return 0
        if left <= start and end <= right: return self.tree[i]
        mid = (start + end) // 2
        return self.search(start, mid, left, right, i*2) + self.search(mid+1, end, left, right, i*2 + 1)
    
    def update(self, start, end, idx, diff, i=1):
        if idx < start or end < idx: return
        self.tree[i] += diff
        if start == end: return
        mid = (start + end) // 2
        self.update(start, mid, idx, diff, i*2)
        self.update(mid+1, end, idx, diff, i*2 + 1)

    def __init__(self, arr):
        self.arr = arr
        self.height = ceil(log(len(arr), 2))
        self.tree = [0] * pow(2, self.height + 1)
        self.segment(0, len(arr) - 1)
    
    def __len__(self):
        return len(self.tree) - 1
    
    def __getitem__(self, idx):
        return self.search(1, len(self.arr), idx, idx)
    

segment_tree = SegmentTree(num)
for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        segment_tree.update(1, n, b, c - segment_tree[b])
    else:
        print(segment_tree.search(1, n, b, c))