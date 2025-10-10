n = list(map(int, input().strip()))

if len(n) == 1:
    print('NO')
    exit()

flag = False
for i in range(1, len(n)):
    a, b = n[0], n[-1]
    for j in range(1, i):
        a *= n[j]
    for j in range(i, len(n)-1):
        b *= n[j]
    flag |= a == b
    
print('YES' if flag else 'NO')