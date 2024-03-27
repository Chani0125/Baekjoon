n, k = map(int, input().split())
yos = []
num = list(range(1, n+1))
idx = -1
while len(num) != 0:
    idx = (idx + k) % len(num)
    yos.append(num.pop(idx))
    idx -= 1
print("<" + ", ".join(map(str, yos)) + ">")
