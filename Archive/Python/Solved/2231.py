N = int(input())

nums = []
for i in range(1, N):
    if i + sum(map(int, str(i))) == N:
        print(i)
        break
else:
    print(0)
