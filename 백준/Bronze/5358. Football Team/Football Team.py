import sys

a = sys.stdin.readlines()
for i in range(len(a)):
    a[i] = a[i].replace('e', '-')
    a[i] = a[i].replace('i', 'e')
    a[i] = a[i].replace('-', 'i')
    a[i] = a[i].replace('E', '-')
    a[i] = a[i].replace('I', 'E')
    a[i] = a[i].replace('-', 'I')
print(*a, sep='')