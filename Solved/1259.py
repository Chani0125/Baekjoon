while True:
    n = list(input())
    if n == ["0"]:
        break
    rn = n[::-1]
    if n == rn:
        print("yes")
    else:
        print("no")
