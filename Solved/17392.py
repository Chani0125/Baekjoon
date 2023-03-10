N, M = map(int, input().split())
H = list(map(int, input().split()))

depression = 0
dep_day = M - sum(H) - N

if dep_day > 0:
    Q, R = divmod(dep_day, N+1)
    depression += (Q * (Q+1) * (2*Q+1) // 6 * (N+1)) + (((Q+1) ** 2) * R)

print(depression)
