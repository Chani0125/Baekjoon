import sys

n = int(sys.stdin.readline())
scores = [0, ] + [int(sys.stdin.readline().strip()) for _ in range(n)]

if n < 3:
    print(sum(scores))
else:
    stairs = scores[-2::-1]
    record = [stairs[0], stairs[1], stairs[2] + stairs[0]]
    for i in range(3, n-1):
        record.append(stairs[i] + min(record[i-2], record[i-3]))
    print(sum(scores) - min(record[-3:]))
