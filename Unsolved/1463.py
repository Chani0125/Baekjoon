import sys


def div(depths, n, d):
    if n == 1:
        depths.append(d)
        return True
    set_div = divmod(n, 3)
    if set_div[1] == 0:
        div(depths, set_div[0], d + 1)
        return True
    set_div = divmod(n, 2)
    if set_div[1] == 0:
        div(depths, set_div[0], d + 1)
    div(depths, n - 1, d + 1)


n = int(sys.stdin.readline())
depths = []
div(depths, n, 0)
print(min(depths))
