N = int(input())
t = list(map(int, input().split()))
a = {}
for i in t:
    if i in a:
        a[i] += 1
    else:
        a[i] = 1
M = int(input())
b = list(map(int, input().split()))

for i in b:
    if i in a:
        print(a[i], end=" ")
    else:
        print(0, end=" ")


