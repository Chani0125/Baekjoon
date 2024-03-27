import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())
d = int(input())
a = (a + (b + (c + d) // 60) // 60) % 24
b = (b + (c + d) // 60) % 60
c = (c + d) % 60
print(a, b, c)