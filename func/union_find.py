class union_find:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.r = [0] * n

    def find(self, x) -> int:
        if self.p[x] == x: return x
        self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        x_r = self.find(x)
        y_r = self.find(y)
        if x_r == y_r: return
        if self.r[x_r] < self.r[y_r]:
            self.p[x_r] = y_r
        elif self.r[x_r] > self.r[y_r]:
            self.p[y_r] = x_r
        else:
            self.p[y_r] = x_r
            self.r[x_r] += 1
