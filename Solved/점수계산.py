n = int(input())
a = map(int, input().split())
b, c = 0, 0
for i in a:
    if i: b += 1
    else: b = 0
    c += b * i
print(c)