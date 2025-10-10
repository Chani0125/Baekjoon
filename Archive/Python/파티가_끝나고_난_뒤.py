import sys
input = sys.stdin.readline
l, p = map(int, input().split())
a = [int(i)-p*l for i in input().split()]
print(*a)
