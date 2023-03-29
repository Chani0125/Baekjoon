import sys


t = int(sys.stdin.readline())
for _ in range(t):
    f = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    a = eval(sys.stdin.readline())
    r = 0
    s = 0
    e = len(a)
    for i in f:
        if i == "R":
            r = 1 - r
        else:
            if r == 0:
                s += 1
            else:
                e -= 1
    if s > e:
        print("error")
    else:
        if r == 0 or s == r:
            a = a[s:e]
        else:
            if s == 0:
                a = a[e - 1::-1]
            else:
                a = a[e-1:s-1:-1]
        print("[" + ",".join(map(str, a)) + "]")
