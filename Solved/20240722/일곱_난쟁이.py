import sys

a = [int(sys.stdin.readline()) for _ in range(9)]
a.sort()
sum_a = sum(a)

for i in range(9):
    for j in range(i+1, 9):
        if sum_a - a[i] - a[j] == 100:
            for k in range(9):
                if k != i and k != j:
                    print(a[k])
            exit()
