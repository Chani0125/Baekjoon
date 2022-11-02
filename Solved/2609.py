a, b = map(int, input().split())
m = a * b
while not b == 0:
    r = a % b
    a = b
    b = r
print(a)
print(m // a)
