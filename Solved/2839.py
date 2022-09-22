N = int(input())
W3, W5 = 0, 0

while N > 0 and not N % 5 == 0:
    N -= 3
    W3 += 1

if N < 0:
    print(-1)
else:
    W5 = N // 5
    print(W3 + W5)
