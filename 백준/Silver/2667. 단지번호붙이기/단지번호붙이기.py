def find_house(x, y, i):
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for a, b in d:
        if x+a < 0 or y+b < 0:
            continue
        try:
            if house[x+a][y+b] == 1:
                num_house[i] += 1
                house[x+a][y+b] = 0
                find_house(x+a, y+b, i)
            else:
                continue
        except IndexError:
            continue
    return 0


n = int(input())
house = [list(map(int, list(input()))) for i in range(n)]
num_house = []
idx = 0
for i in range(len(house)):
    for j in range(len(house[i])):
        if house[i][j] == 1:
            num_house.append(1)
            house[i][j] = 0
            find_house(i, j, idx)
            idx += 1
print(len(num_house))
num_house.sort()
for i in num_house:
    print(i)