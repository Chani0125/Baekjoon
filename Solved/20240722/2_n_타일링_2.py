n = int(input())

a = [1, 1]
while len(a) <= n:
    a.append((a[-2]*2 + a[-1]) % 10007)
print(a[-1])