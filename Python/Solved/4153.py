while True:
    l = sorted(list(map(int, input().split())))
    for i in range(3):
        if not l[i] == 0:
            break
    else:
        break
    if l[0]**2 + l[1]**2 == l[2]**2:
        print("right")
    else:
        print("wrong")
