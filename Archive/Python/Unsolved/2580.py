def find_line(b, idx, v):
    s = set(range(1, 10))
    blank_idx = []
    for i in range(9):
        if v:
            if type(b[i][idx]) == set:
                s = s - b[i][idx]
            else:
                if b[i][idx] != 0:
                    s.remove(b[i][idx])
                else:
                    blank_idx.append(i)
        else:
            if type(b[idx][i]) == set:
                s = s - b[idx][i]
            else:
                if b[idx][i] != 0:
                    s.remove(b[idx][i])
                else:
                    blank_idx.append(i)
    if len(blank_idx) == 1:
        if v:
            b[blank_idx[0]][idx] = s.pop()
        else:
            b[idx][blank_idx[0]] = s.pop()
        return True
    else:
        if v:
            for blk_idx in blank_idx:
                b[blk_idx][idx] = s
        else:
            for blk_idx in blank_idx:
                b[idx][blk_idx] = s
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
        if b[i][j] == 0:
            blank_list.append((i, j))
while True:
    for i in range(9):
        find_line(b, i, True)
        find_line(b, i, False)
    for i in range(3):
        for j in range(3):
            find_square(b, i, j)
    for i in b:
        tmp = True
        for j in i:
            if type(j) == set:
                tmp = False
                break
            elif j == 0:
                tmp = False
                break
        if not tmp:
            break
    else:
        break

for line in b:
    print(" ".join(map(str, line)))
print()
