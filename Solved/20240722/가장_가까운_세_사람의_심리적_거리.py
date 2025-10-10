import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    arr = [*map(list, input().split())]

    a = [0] * n
    for i in range(n):
        if arr[i][0] == 'I':
            a[i] += 8
        if arr[i][1] == 'N':
            a[i] += 4
        if arr[i][2] == 'F':
            a[i] += 2
        if arr[i][3] == 'P':
            a[i] += 1
    
    ans = 125
    for i in range(16):
        b = sorted(a, key=lambda x: sum(map(int, bin(i^x)[2:])))
        
        p = sum(map(int, bin(b[0]^b[1])[2:]))
        q = sum(map(int, bin(b[1]^b[2])[2:]))
        r = sum(map(int, bin(b[2]^b[0])[2:]))
        
        ans = min(ans, p+q+r)
    
    print(ans)
