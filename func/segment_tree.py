class SegmentTree:
    def segment(self, s, e, idx=1) -> int:
        if s == e:
            self.tree[idx] = self.arr[s]
            return self.tree[idx]
        m = (s + e) // 2
        self.tree[idx] = self.segment(s, m, idx*2) + self.segment(m+1, e, idx*2+1)
        return self.tree[idx]
    
    def search(self, s, e, l, r, idx=1) -> int:
        if e < l or r < s: return 0
        if l <= s and e <= r: return self.tree[idx]
        mid = (s + e) // 2
        return self.search(s, mid, l, r, idx*2) + self.search(mid+1, e, l, r, idx*2+1)
    
    def update(self, s, e, arr_idx, diff, idx=1):
        if arr_idx < s or e < arr_idx: return
        self.tree[idx] += diff
        if s == e: return
        mid = (s + e) // 2
        self.update(s, mid, arr_idx, diff, idx*2)
        self.update(mid+1, e, arr_idx, diff, idx*2+1)

    def __init__(self, arr):
        self.arr = arr
        self.height = len(arr).bit_length()
        self.tree = [0] * (2 << self.height)
        self.segment(0, len(arr) - 1)
    
    def __len__(self) -> int:
        return len(self.tree) - 1
    
    def __getitem__(self, idx) -> int:
        return self.search(0, len(self.arr)-1, idx, idx)