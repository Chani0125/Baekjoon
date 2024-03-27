import sys
from math import log2, ceil

n = int(sys.stdin.readline())
print(ceil(log2(n) + 1) if n else 0)