import sys

n, a, w = sys.stdin.readline().split()
while n != '#':
    if (int(a) > 17 or int(w) >= 80):
        print(n, 'Senior')
    else:
        print(n, 'Junior')
    n, a, w = sys.stdin.readline().split()