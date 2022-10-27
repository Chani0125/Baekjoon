while True:
    n = int(input())
    if n == 0:
        break
    units = input().split()
    r = []
    for i in range(n-1):
        tmp0 = input().split(" = ")
        tmp1 = tmp0[1].split()
        r.append([tmp0[0], int(tmp1[0]), tmp1[1]])

    print(r)

