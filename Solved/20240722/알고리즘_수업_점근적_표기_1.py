a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

while n0 <= 100:
    if n0 * (c-a1) >= a0:
        n0 += 1
    else:
        break
else:
    print(1)
    exit()
print(0)