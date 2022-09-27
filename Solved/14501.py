import sys
# import time


def consult(t, p, total):
    if len(t) == 1:
        if t[0] == 1:
            return total + p[0]
        else:
            return total
    elif t[0] > len(t):
        a = consult(t[1:], p[1:], total)
        b = total
        if a > b:
            return a
        else:
            return b
    elif t[0] == 1:
        return consult(t[1:], p[1:], total) + p[0]
    elif t[0] == len(t):
        a = total + p[0]
        b = consult(t[1:], p[1:], total)
        if a > b:
            return a
        else:
            return b
    else:
        a = consult(t[1:], p[1:], total)
        b = consult(t[t[0]:], p[t[0]:], total) + p[0]
        if a > b:
            return a
        else:
            return b


N = int(sys.stdin.readline())
T = []
P = []
for i in range(N):
    time, pay = map(int, sys.stdin.readline().split())
    T.append(time)
    P.append(pay)

# start = time.time()

print(consult(T, P, 0))

# print(time.time() - start)
