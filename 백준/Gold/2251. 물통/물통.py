a, b, c = map(int, input().split())

v = [[[False] * (c+1) for _ in range(b+1)] for _ in range(a+1)]

def water(x, y, z):    
    if v[x][y][z]: return
    v[x][y][z] = True
    
    if x < a:
        water(min(a, x+y), x+y-a if x+y > a else 0, z)
        water(min(a, x+z), y, x+z-a if x+z > a else 0)
    if y < b:
        water(y+x-b if y+x > b else 0, min(b, y+x), z)
        water(x, min(b, y+z), y+z-b if y+z > b else 0)
    if z < c:
        water(z+x-c if z+x > c else 0, y, min(c, z+x))
        water(x, z+y-c if z+y > c else 0, min(c, z+y))

water(0, 0, c)

u = set()
for i in range(b+1):
    for j in range(c+1):
        if v[0][i][j]: u.add(j)
print(*sorted([*u]), sep=' ')