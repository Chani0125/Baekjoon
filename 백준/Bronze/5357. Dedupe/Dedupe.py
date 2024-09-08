n = int(input())

for _ in range(n):
    a = input().strip()
    for i in range(len(a)):
        if a[i] != a[i-1] or i == 0:
            print(a[i], end='')
    print()