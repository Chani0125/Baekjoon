n = int(input())

if n == 0:
    print('*')
    exit()
    
if n == 1:
    print('  *  ')
    print('  *  ')
    print('*****')
    print(' *** ')
    print(' * * ')
    exit()

star = [
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0]
]

blank = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

from copy import deepcopy

ans = deepcopy(star)

def make_star(arr):
    for i in range(5):
        for j in range(5):
            if type(arr[i][j]) == type(list()):
                make_star(arr[i][j])
            else:
                if arr[i][j] == 1:
                    arr[i][j] = deepcopy(star)
                else:
                    arr[i][j] = deepcopy(blank)

for _ in range(n-1):
    make_star(ans)

if n == 2:
    for i in range(25):
        for j in range(25):
            print('*' if ans[i//5][j//5][i%5][j%5] else ' ', end='')
        print()
            
if n == 3:
    for i in range(125):
        for j in range(125):
            print('*' if ans[i//25][j//25][(i//5)%5][(j//5)%5][i%5][j%5] else ' ', end='')
        print()
            
if n == 4:
    for i in range(625):
        for j in range(625):
            print('*' if ans[i//125][j//125][(i//25)%5][(j//25)%5][(i//5)%5][(j//5)%5][i%5][j%5] else ' ', end='')
        print()
            
if n == 5:
    for i in range(3125):
        for j in range(3125):
            print('*' if ans[i//625][j//625][(i//125)%5][(j//125)%5][(i//25)%5][(j//25)%5][(i//5)%5][(j//5)%5][i%5][j%5] else ' ', end='')
        print()

# print(ans)
