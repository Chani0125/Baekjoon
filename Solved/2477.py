K = int(input())
d = []
l = []
for i in range(6):
    a, b = map(int, input().split())
    d.append(a)
    l.append(b)
d.extend(d)
l.extend(l)
if d[d.index(4):d.index(4)+6] == [4, 2, 3, 1, 3, 1]:
    idx = d.index(4)
    chamoe = (l[idx] * l[idx+1] - l[idx+3] * l[idx+4]) * K
elif d[d.index(2):d.index(2)+6] == [2, 3, 1, 4, 1, 4]:
    idx = d.index(2)
    chamoe = (l[idx] * l[idx+1] - l[idx+3] * l[idx+4]) * K
elif d[d.index(3):d.index(3)+6] == [3, 1, 4, 2, 4, 2]:
    idx = d.index(3)
    chamoe = (l[idx] * l[idx+1] - l[idx+3] * l[idx+4]) * K
else:
    idx = d.index(1)
    chamoe = (l[idx] * l[idx+1] - l[idx+3] * l[idx+4]) * K

print(chamoe)

# [4, 2, 3, 1, 3, 1]
# [2, 3, 1, 4, 1, 4]
# [3, 1, 4, 2, 4, 2]
# [1, 4, 2, 3, 2, 3]
