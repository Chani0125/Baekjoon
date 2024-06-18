import sys

n = int(sys.stdin.readline())

a = [0, 0, 1]
for i in range(3, n+1):
    a[i%3] = ((i-1) * (a[(i-1)%3] + a[(i-2)%3])) % 1000000000
print(a[n%3] % 1000000000)

