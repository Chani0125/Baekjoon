T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    Y = (N-1) % H + 1
    X = (N-1) // H + 1
    print(Y, end="")
    if X < 10:
        print(f"0{X}")
    else:
        print(X)
