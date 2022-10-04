import sys


N = int(sys.stdin.readline())
Sangeun_card = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
decide_card = list(map(int, sys.stdin.readline().split()))

for i in decide_card:
    if i in Sangeun_card:
        print(1, end=" ")
        # Sangeun_card.remove(i)
    else:
        print(0, end=" ")