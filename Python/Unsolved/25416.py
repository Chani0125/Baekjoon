import sys
sys.setrecursionlimit(10**5)


def movement(x, y, a):
    print(x, y)
    d = a[:]
    d[y][x] = True
    for i in range(5):
        print(arr[i], d[i])
    print()
    nums = []
    for dx, dy in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
        print(x + dx, y + dy)
        if x + dx > 4 or x + dx < 0 or y + dy > 4 or y + dy < 0:
            continue
        print(d[y + dy][x + dx])
        if d[y + dy][x + dx]:
            print("t1")
            continue
        elif arr[y + dy][x + dx] == 1:
            print("t2")
            return 1
        elif arr[y + dy][x + dx] == -1:
            print("t3")
            continue
        else:
            move = movement(x + dx, y + dy, d[:])
            if move == -1:
                continue
            else:
                nums.append(move + 1)
                print(move + 1, x, y)
    if len(nums) == 0:
        return -1
    else:
        return min(nums)


arr = [list(map(int, input().split())) for _ in range(5)]
arr2 = [[False for j in range(5)] for i in range(5)]
r, c = map(int, input().split())
print(movement(r, c, arr2[:]))
