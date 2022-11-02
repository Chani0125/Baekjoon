n, k = map(int, input().split())
up5 = 0
up2 = 0
down5 = 0
down2 = 0
for i in range(k):
    if n-i == 5:
        up5 += 1
    elif n-i == 2:
        up2 += 1
    if i+1 == 5:
        down5 += 1
    elif i+1 == 2:
        down2 += 1
total5 = up5 - down5
total2 = up2 - down2
print(min([total5, total2]))
