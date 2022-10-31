a, b = map(int, input().split())
fac_v = []
i = 2
while i <= a and i <= b:
    if a % i == 0 and b % i == 0:
        fac_v.append(i)
        a //= i
        b //= i
    else:
        i += 1
m = 1
for i in fac_v:
    m *= i
print(m)
print(m * a * b)
