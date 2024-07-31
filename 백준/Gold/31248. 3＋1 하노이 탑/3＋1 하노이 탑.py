n = int(input())

def hanoi(k, a, b, c):
    global n
    
    # 마지막 원판을 옮기는 경우
    if k == 1:
        # 마지막 원판을 D로 옮기는 경우
        if k == n:
            print(a, 'D')
        # 일반적인 하노이탑의 이동의 경우
        else:
            print(a, c)
        return
    
    # 밑에 2칸을 D로 옮기는 경우
    if k == n:
        if k < 3:
            hanoi(k-1, a, c, b)
            print(a, 'D')
            n -= 1
            hanoi(k-1, b, a, c)
        else:
            hanoi(k-2, a, c, b)
            print(a, c)
            print(a, 'D')
            print(c, 'D')
            n -= 2
            hanoi(k-2, b, a, c)
    
    # 일반적인 하노이탑의 이동의 경우
    else:
        hanoi(k-1, a, c, b)
        print(a, c)
        hanoi(k-1, b, a, c)


a = 0
# 2칸 빼고 위의 하노이탑을 이동하는 경우의 수
for i in range(n-2, -1, -2):
    a += pow(2, i) + 2
if n % 2: a += 1

print(a)
hanoi(n, 'A', 'B', 'C')