N, M = map(int, input().split())
A = set([input() for i in range(N)])
B = set([input() for i in range(M)])

n = 0
ans = []
for i in A:
    if i in B:
        n += 1
        ans.append(i)

print(n)
print("\n".join(sorted(ans)))
