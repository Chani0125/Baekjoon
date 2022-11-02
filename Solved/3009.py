x = {}
y = {}
for i in range(3):
    a, b = map(int, input().split())
    if a in x:
        x[a] += 1
    else:
        x[a] = 1
    if b in y:
        y[b] += 1
    else:
        y[b] = 1

for key, val in x.items():
    if val == 1:
        print(key, end=" ")

for key, val in y.items():
    if val == 1:
        print(key)