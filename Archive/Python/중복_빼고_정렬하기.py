import sys

input = sys.stdin.readline
n = int(input())
a = set(map(int, input().split()))
print(' '.join(map(str, sorted(a))))