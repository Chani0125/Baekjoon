import sys

n = int(sys.stdin.readline())

coord = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
coord.sort(key=lambda x: x[0])

start = [x for x, y in coord]
end = [y for x, y in coord]

num_start = {}
num_end = {}
for s, e in coord:
    if s in num_start:
        num_start[s] += 1
    else:
        num_start[s] = 1
    if e in num_end:
        num_end[e] += 1
    else:
        num_end[e] = 1

coord_change = sorted(list(set(start) | set(end)))
max_value = 0
current_value = 0
for i in coord_change:
    if i in num_start:
        current_value += num_start[i]
    if i in num_end:
        current_value -= num_end[i]
    max_value = max(max_value, current_value)

print(max_value)