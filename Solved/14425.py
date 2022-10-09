N, M = map(int, input().split())
S = set([input() for i in range(N)])
W = [input() for i in range(M)]
ans = 0

for i in W:
    if i in S:
        ans += 1

print(ans)
