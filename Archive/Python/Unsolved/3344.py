n = int(input())
r_up = set()
r_down = set()
v = set()
ans = []
for x in range(n):
    for y in range(n):
        if y in v:
            continue
        if x + y in r_up:
            continue
        if x - y in r_down:
            continue
        ans.append(y)
        break
    if len(ans) != x + 1:
        ans = []