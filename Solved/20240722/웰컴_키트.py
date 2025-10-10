import sys

input = sys.stdin.readline

n = int(input())
s = [*map(int, input().split())]
t, p = map(int, input().split())

print(sum(map(lambda x: (x+t-1)//t, s)))
print(*divmod(n, p))