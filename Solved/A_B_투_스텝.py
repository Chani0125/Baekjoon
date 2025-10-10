t = int(input())

if t == 1:
    a, b = map(int, input().split())
    p = a + b
    arr = ''
    for i in range(13):
        arr += chr(ord('a') + p % 26)
        p //= 26  
    print(arr)
else:
    arr = input().strip()
    ans = 0
    for i in range(13):
        ans += (ord(arr[i])-ord('a')) * (26 ** i)
    print(ans)