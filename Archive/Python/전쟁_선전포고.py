import sys

input = sys.stdin.readline

n, m = map(int, input().split())

p_c = []
p_v = []
for _ in range(n):
    a, b = input().split()
    p_c.append(eval(a))
    p_v.append(int(b))

lines = []
for _ in 