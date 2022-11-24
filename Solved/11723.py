import sys


a = set()
for _ in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().split()
    if s[0] == "add":
        a.add(int(s[1]))
    elif s[0] == "remove":
        if int(s[1]) in a:
            a.remove(int(s[1]))
    elif s[0] == "check":
        if int(s[1]) in a:
            print(1)
        else:
            print(0)
    elif s[0] == "toggle":
        if int(s[1]) in a:
            a.remove(int(s[1]))
        else:
            a.add(int(s[1]))
    elif s[0] == "all":
        a = set(range(1, 21))
    elif s[0] == "empty":
        a = set()
