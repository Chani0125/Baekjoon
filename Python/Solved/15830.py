from decimal import Decimal
import math

V, W, D = map(Decimal, input().split())
N = 0

while D > 0:
    take_time = W / V
    D -= Decimal(5 * math.pow(take_time, 2))
    V *= Decimal('0.8')
    if D > 0:
        N += 1
    # print(f"V: {V}, W: {W}, D: {D}, N: {N}, T: {take_time}, Take: {5 * take_time ** 2}")

print(N)
