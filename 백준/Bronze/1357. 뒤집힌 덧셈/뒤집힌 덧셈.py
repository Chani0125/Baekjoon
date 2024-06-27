x, y = map(list, input().split())
x = map(int, x)
y = map(int, y)

z = 0
for idx, val in enumerate(x):
    z += (10 ** idx) * val
for idx, val in enumerate(y):
    z += (10 ** idx) * val
print(int(str(z)[::-1]))