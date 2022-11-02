n = int(input())
r = list(map(int, input().split()))
for i in range(1, len(r)):
    if r[0] > r[i]:
        a, b = r[0], r[i]
    else:
        a, b = r[i], r[0]
    while not b == 0:
        re = a % b
        a = b
        b = re
    print(f"{r[0]//a}/{r[i]//a}")