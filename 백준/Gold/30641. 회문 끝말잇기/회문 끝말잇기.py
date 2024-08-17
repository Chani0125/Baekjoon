l, u = map(int, input().split())

DIVIDER = 1000000007

p = [pow(26, ((i-1) // 2), DIVIDER) for i in range(l, u+1)]
s = sum(p) % DIVIDER

if l == 2 or (l == 1 and u == 1):
    print('H')
else:
    print('A')
    
print(s)
