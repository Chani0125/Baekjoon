import sys


num_bit = [0, 1] + [2**(i-1) + (2**(i-2) * (i-1)) for i in range(2, 60)]

a, b = map(int, sys.stdin.readline().split())

a_bin = [*map(int, bin(a)[2:])]
b_bin = [*map(int, bin(b)[2:])]

res = sum(num_bit[len(a_bin):len(b_bin)])

for idx, val in enumerate(a_bin[-1:0:-1]):
    if val: res -= sum(num_bit[:idx+1]) + (2 ** idx) * sum(a_bin[:-idx-1])

for idx, val in enumerate(b_bin[-1:0:-1]):
    if val: res += sum(num_bit[:idx+1]) + (2 ** idx) * sum(b_bin[:-idx-1])
res += sum(b_bin)

print(res)
