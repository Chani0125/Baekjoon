n = [int(input()) for _ in range(3)]
n = list(map(int, list(str(n[0] * n[1] * n[2]))))
c = [0 for i in range(10)]
for num in n:
    c[num] += 1
print("\n".join(map(str, c)))
