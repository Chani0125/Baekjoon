N, M = map(int, input().split())
A = {}
B = {}
for i in range(N):
    t = input()
    A[i+1] = t
    B[t] = i+1
P = [input() for i in range(M)]

for i in P:
    try:
        print(A[int(i)])
    except ValueError:
        print(B[i])