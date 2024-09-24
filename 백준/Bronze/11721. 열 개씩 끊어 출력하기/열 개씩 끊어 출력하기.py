a = input().strip()
for idx, c in enumerate(a):
    if idx % 10 == 0 and idx:
        print()
    print(c, end='')