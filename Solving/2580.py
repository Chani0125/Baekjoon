def find_line(b, idx, v):
    s = set(range(1, 10))
    for i in range(9):
        if v:
            if b[i][idx] != 0:
                s.remove(b[i][idx])
            else:
                blank_idx = i
        else:
            if b[idx][i] != 0:
                s.remove(b[idx][i])
            else:
                blank_idx = i
    if len(s) == 1:
        if v:
            b[blank_idx][idx] = s.pop()
        else:
            b[idx][blank_idx] = s.pop()
        return True
    return False


def find_square(b, v_idx, h_idx):
    s = set(range(1, 10))
    blank_idx = []
    for i in range(v_idx * 3, v_idx * 3 + 3):
        for j in range(h_idx * 3, h_idx * 3 + 3):
            if b[i][j] != 0:
                s.remove(b[i][j])
            else:
                blank_idx.append((i, j))
    if len(s) == 1:
        b[blank_idx[0]][blank_idx[1]] = s.pop()
        return True
    return False


b = [list(map(int, input().split())) for _ in range(9)]
blank_list = []
for i in range(9):
    for j in range(9):
        if b[i][j] == 0 or type(b[i][j]) == set:
            blank_list.append((i, j))
while True:
    for i in range(9):
        find_line(b, i, True)
        find_line(b, i, False)
    for i in range(3):
        for j in range(3):
            find_square(b, i, j)
    for i in b:
        if 0 in i:
            break
    else:
        break

for line in b:
    print(" ".join(map(str, line)))
print()
