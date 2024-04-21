n = int(input())
l = 1

while n > l:
    n -= l
    l += 1

if l % 2 == 1:
    nu = l
    for i in range(n-1):
        nu -= 1
else:
    nu = 1
    for i in range(n-1):
        nu += 1

print(f"{nu}/{l+1-nu}")