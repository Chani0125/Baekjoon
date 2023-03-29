def factorial(n, ans):
    if n == 0:
        return 1
    elif n == 1:
        return ans
    else:
        return factorial(n-1, ans * n)


print(factorial(int(input()), 1))
