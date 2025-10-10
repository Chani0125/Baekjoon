a = [int(input()) for _ in range(7)]

b = [i for i in a if i % 2]

if b:
    print(sum(b))
    print(min(b))
else:
    print(-1)