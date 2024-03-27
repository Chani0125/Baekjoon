n, k = map(int, input().split())
f = [0, 0]
fac = [(2, 0), (5, 1)]
for factor, idx in fac:
    i = factor
    while i <= n:
        f[idx] += n // i - (n-k) // i
        f[idx] -= k // i
        i *= factor
print(min(f))
