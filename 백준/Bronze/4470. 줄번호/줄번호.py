import sys
input = sys.stdin.readline
n = int(input())
arr = [input() for _ in range(n)]
for idx, str in enumerate(arr):
    print(f'{idx + 1}. {str}', end='')