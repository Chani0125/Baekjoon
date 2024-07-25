import sys

input = sys.stdin.readline

x, y = input().split()
while x != '0' or y != '0':
    if x == '0' or y == '0':
        print('AXIS')
    elif x[0] == '-':
        if y[0] == '-':
            print('Q3')
        else:
            print('Q2')
    else:
        if y[0] == '-':
            print('Q4')
        else:
            print('Q1')
    x, y = input().split()
print('AXIS')