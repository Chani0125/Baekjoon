import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(input().strip()) for _ in range(n)]

p = sum(['X' not in i for i in a])
q = sum(['X' not in i for i in zip(*a)])

print(max(p, q))