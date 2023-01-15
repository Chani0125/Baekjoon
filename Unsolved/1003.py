def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        if fibo_list[n] == 0:
            fibo_list[n] = fibo(n-1) + fibo(n-2)
        return fibo_list[n]


t = int(input())
fibo_list = [0 for _ in range(41)]
fibo_list[1] = 1
for _ in range(t):
    arr = list(str(fibo(int(input()))))
    zero, one = 0, 0
    for i in arr:
        if i == "0":
            zero += 1
        elif i == "1":
            one += 1
    print(zero, one)
