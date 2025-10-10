import sys

n = int(sys.stdin.readline())
v = []
for _ in range(n):
    x1, x2, y = sys.stdin.readline().split()
    if y.strip() == 'LOVELYZ':
        v.append((int(x1), int(x2), 1))
    else:    
        v.append((int(x1), int(x2), 0))

iter = 1000
for epoch in range(iter):
    pass