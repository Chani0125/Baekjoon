def find_bridge(a, b):
    if not bridge[a-1][b-1] == -1:
        return bridge[a-1][b-1]
    else:
        if a == b:
            val = 1
        elif a == 1:
            val = b
        else:
            val = 0
            for i in range(1, b-a+2):
                val += find_bridge(a-1, b-i)
        bridge[a-1][b-1] = val
        return val


t = int(input())
bridge = [[-1 for j in range(30)] for i in range(30)]
for i in range(t):
    n, m = map(int, input().split())
    print(find_bridge(n, m))
