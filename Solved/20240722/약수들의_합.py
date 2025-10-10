import sys

def devider(n):
    deviders = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            deviders.append(i)
    return deviders

input = sys.stdin.readline
n = int(input())
while n != -1:
    d = devider(n)
    if sum(d) == n:
        print(f"{n} = {' + '.join(map(str, d))}")
    else:
        print(f"{n} is NOT perfect.")
    n = int(input())