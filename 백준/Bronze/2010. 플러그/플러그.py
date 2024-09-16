import sys

input = sys.stdin.readline

n = int(input())
a = [int(input()) for _ in range(n)]

print(sum(a)-n+1)