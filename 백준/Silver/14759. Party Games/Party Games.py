import sys

input = sys.stdin.readline
n = int(input())

while n:
    v = [input().strip() for _ in range(n)]
    v.sort()
    
    a, b = v[(n>>1)-1], v[n>>1]
    c = -1
    if len(a) < len(b):
        for i in range(len(a)):
            if a[i] != b[i]:
                c = i
                break
        else:
            print(a)
            n = int(input())
            continue
        
    elif len(a) > len(b):
        for i in range(len(b)):
            if a[i] != b[i]:
                c = i
                break
    else:
        for i in range(len(a)):
            if a[i] != b[i]:
                c = i
                break

    ans = a[:c]
    if c == len(a)-1:
        ans += a[c]
    else:
        if c == len(b)-1 and ord(b[c]) == ord(a[c])+1:
            for i in range(c+1, len(a)-1):
                if a[i] != 'Z':
                    ans += a[c:i] + chr(ord(a[i])+1)
                    break
            else:
                ans += a[c:]
        else:
            ans += chr(ord(a[c])+1)
    print(ans)
    
    n = int(input())