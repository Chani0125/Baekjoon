a, b = map(int, input().split())
m, n = a+b, a-b

if (m%2 or n%2 or n<0): print(-1)
else: print(m//2, n//2)