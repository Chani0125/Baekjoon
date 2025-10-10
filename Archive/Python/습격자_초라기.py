import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n, w = map(int, input().split())
    a = []
    a.append([*map(int, input().split())])
    a.append([*map(int, input().split())])
    
    # 0: 혼자, 1: 위아래, 2: 왼쪽, 3: 오른쪽
    b = [[[] for _ in range(n)] for _ in range(2)]
    
    for i in range(n):
        if a[0][i] + a[1][i] <= w:
            b[0][i].append(1)
            b[1][i].append(1)
        
        for j in range(2):
            if a[j][i] + a[j][i-1] <= w:
                b[j][i].append(2)
            if a[j][i] + a[j][(i+1)%n] <= w:
                b[j][i].append(3)
    
    print(*a, sep='\n')
    print(*b, sep='\n')
    print(*map(len, b[0]), sep=' ')
    print(*map(len, b[1]), sep=' ')