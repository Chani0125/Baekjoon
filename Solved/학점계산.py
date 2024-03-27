import sys

grade = sys.stdin.readline().strip()

if grade[0] == 'A':
    int_part = 4
elif grade[0] == 'B':
    int_part = 3
elif grade[0] == 'C':
    int_part = 2
elif grade[0] == 'D':
    int_part = 1
else:
    int_part = 0

if len(grade) == 2:
    if grade[1] == '+':
        float_part = 3
    elif grade[1] == '-':
        int_part -= 1
        float_part = 7
    else:
        float_part = 0
else:
    float_part = 0

print(f'{int_part}.{float_part}')
