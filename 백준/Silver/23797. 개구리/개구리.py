import sys

arr = list(sys.stdin.readline().strip())

ans = 0
p, k = 0, 0
for i in arr:
    if i == 'P':
        if k: k -= 1
        p += 1
    if i == 'K':
        if p: p -= 1
        k += 1
    
print(p + k)