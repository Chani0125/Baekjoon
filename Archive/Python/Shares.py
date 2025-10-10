import sys

inputs = sys.stdin.readlines()
for s in inputs:
    a, b = map(int, s.split())
    print(b // (a+1))