import sys
input = sys.stdin.readline
n = int(input())
strs = [input().strip() for _ in range(n)]
for str in strs:
    print(str.lower())
