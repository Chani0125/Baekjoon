import sys

input = sys.stdin.readline
t = int(input())

v = [[i] for i in range(10)]
for i in range(10):
    while (v[i][-1] * i) % 10 != i:
        v[i].append((v[i][-1] * i) % 10)
v[0][0] = 10

for _ in range(t):
    a, b = map(int, input().split()) 
    if b == 0:
        print(1)
    else:
        print(v[a%10][(b-1) % len(v[a%10])])