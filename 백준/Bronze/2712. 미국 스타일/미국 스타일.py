from decimal import Decimal
import sys

input = sys.stdin.readline

n = int(input())
d = {'kg': (22046, 'lb'), 'lb': (4536, 'kg'), 'l': (2642, 'g'), 'g': (37854, 'l')}

for _ in range(n):
    a, b = input().split()
    print(f'{Decimal(a) * d[b][0] / 10000:.4f} {d[b][1]}')