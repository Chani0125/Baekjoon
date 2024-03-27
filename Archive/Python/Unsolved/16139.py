import sys


s = sys.stdin.readline().strip()
q = int(sys.stdin.readline())
alphabet = [[] for _ in range(26)]
total = [0 for _ in range(26)]

for letter in s:
    total[ord(letter) - 97] += 1
    for i in range(26):
        alphabet[i].append(total[i])

for i in range(q):
    c, start, end = sys.stdin.readline().split()
    start = int(start)
    end = int(end)
    if start == 0:
        ans = alphabet[ord(c) - 97][end]
    else:
        ans = alphabet[ord(c) - 97][end] - alphabet[ord(c) - 97][start-1]
    print(ans)
