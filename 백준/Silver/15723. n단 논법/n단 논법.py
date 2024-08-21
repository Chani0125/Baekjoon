import sys

input = sys.stdin.readline

n = int(input())
v = [[0] * 26 for _ in range(26)]
for _ in range(n):
    a, _, b = input().split()
    a = ord(a) - 97
    b = ord(b) - 97
    v[a][b] = 1

for k in range(26):
    for i in range(26):
        for j in range(26):
            if v[i][k] and v[k][j]:
                v[i][j] = 1

m = int(input())
for _ in range(m):
    a, _, b = input().split()
    a = ord(a) - 97
    b = ord(b) - 97
    print('T' if v[a][b] else 'F')