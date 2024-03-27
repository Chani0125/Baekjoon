def str_star(s, n):
    if s == 3:
        if n % 3 == 1:
            print("* *", end="")
        else:
            print("***", end="")
    else:
        if n % s // (s // 3) == 1:
            str_star(s // 3, n)
            print(" " * (s // 3), end="")
            str_star(s // 3, n)
        else:
            for j in range(3):
                str_star(s // 3, n)


def make_star(s):
    if s == 3:
        for i in range(3):
            str_star(3, i)
            print()
    else:
        for i in range(s // 3):
            for j in range(3):
                str_star(s // 3, i)
            print()
        for i in range(s // 3):
            str_star(s // 3, i)
            print(" "*(s//3), end="")
            str_star(s // 3, i)
            print()
        for i in range(s // 3):
            for j in range(3):
                str_star(s // 3, i)
            print()


make_star(int(input()))