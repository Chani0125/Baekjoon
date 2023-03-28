import sys
import heapq

n, m = map(int, sys.stdin.readline().strip().split())
nums = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

tetrominos = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],

    [(0, 0), (0, 1), (1, 0), (1, 1)],

    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 0)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 0), (1, 1), (1, 2)],
    [(0, 1), (1, 1), (2, 0), (2, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 2)],
    [(0, 0), (0, 1), (1, 0), (2, 0)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],

    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(0, 1), (0, 2), (1, 0), (1, 1)],
    [(0, 1), (1, 0), (1, 1), (2, 0)],
    [(0, 0), (0, 1), (1, 1), (1, 2)],

    [(0, 1), (1, 0), (1, 1), (1, 2)],
    [(0, 0), (1, 0), (1, 1), (2, 0)],
    [(0, 1), (1, 0), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 1)]
]

max_sum = 0

for nx in range(n):
    for ny in range(m):
        for tet in tetrominos:
            now_sum = 0
            for dx, dy in tet:
                x = nx + dx
                y = ny + dy
                if 0 <= x < n and 0 <= y < m:
                    now_sum += nums[x][y]
                else:
                    break
            if now_sum > max_sum:
                max_sum = now_sum

print(max_sum)
