n = int(input())
a = input().strip()

ans = 1

for i in range(1, n+1):
    tmp = 0
    
    if a[i:] == a[:n-i]:
        b = a[:i] + a
        
        for j in range(len(b)-n):
            if b[j:j+n] == a:
                tmp += 1
        
        ans = max(ans, tmp)

print(ans)