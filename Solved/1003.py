t = int(input())
for _ in range(t):
    n = int(input())
    zero_one = [[1, 0], [0, 1]]
    if n > 1:
        for i in range(2, n+1):
            zero_one.append([zero_one[i-2][0] + zero_one[i-1][0], zero_one[i-2][1] + zero_one[i-1][1]])
    print(" ".join(map(str, zero_one[n])))
