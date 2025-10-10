import sys
from math import ceil, log

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

class MinSegmentTree:
    def segment(self, left, right, i=1):
        if left == right:
            self.tree[i] = self.arr[left]
            return self.tree[i]
        mid = (left + right) // 2
        self.tree[i] = min(self.segment(left, mid, i*2), self.segment(mid+1, right, i*2 + 1))
        return self.tree[i]
    
    def search(self, start, end, left, right, i=1):
        if end < left or right < start: return 1000000001
        if left <= start and end <= right: return self.tree[i]
        mid = (start + end) // 2
        return min(self.search(start, mid, left, right, i*2), self.search(mid+1, end, left, right, i*2 + 1))
    
    def __init__(self, arr):
        self.arr = arr
        self.height = ceil(log(len(arr), 2))
        self.tree = [0] * pow(2, self.height + 1)
        self.segment(0, len(arr) - 1)
    
    def __len__(self):
        return len(self.tree) - 1
    
    def __getitem__(self, idx):
        return self.search(1, len(self.arr), idx, idx)
    
class MaxSegmentTree:
    def segment(self, left, right, i=1):
        if left == right:
            self.tree[i] = self.arr[left]
            return self.tree[i]
        mid = (left + right) // 2
        self.tree[i] = max(self.segment(left, mid, i*2), self.segment(mid+1, right, i*2 + 1))
        return self.tree[i]
    
    def search(self, start, end, left, right, i=1):
        if end < left or right < start: return 0
        if left <= start and end <= right: return self.tree[i]
        mid = (start + end) // 2
        return max(self.search(start, mid, left, right, i*2), self.search(mid+1, end, left, right, i*2 + 1))
    
    def __init__(self, arr):
        self.arr = arr
        self.height = ceil(log(len(arr), 2))
        self.tree = [0] * pow(2, self.height + 1)
        self.segment(0, len(arr) - 1)
    
    def __len__(self):
        return len(self.tree) - 1
    
    def __getitem__(self, idx):
        return self.search(1, len(self.arr), idx, idx)

min_segment_tree = MinSegmentTree(arr)
max_segment_tree = MaxSegmentTree(arr)
for _ in range(m):
    l, r = map(int, input().split())
    print(min_segment_tree.search(1, n, l, r), max_segment_tree.search(1, n, l, r))
    