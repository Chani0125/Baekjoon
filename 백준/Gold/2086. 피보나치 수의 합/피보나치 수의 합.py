n, m = map(int, input().split())

fibo_mat = [[[1, 1], [1, 0]]]

DIVIER = 1000000000

def inner_product(mat1, mat2):
    a = (mat1[0][0] * mat2[0][0] + mat1[0][1] * mat2[1][0]) % DIVIER
    b = (mat1[0][0] * mat2[0][1] + mat1[0][1] * mat2[1][1]) % DIVIER
    c = (mat1[1][0] * mat2[0][0] + mat1[1][1] * mat2[1][0]) % DIVIER
    d = (mat1[1][0] * mat2[0][1] + mat1[1][1] * mat2[1][1]) % DIVIER
    return [[a, b], [c, d]]

n = n + 1
m = m + 2

for i in range(max(n.bit_length(), m.bit_length())):
    fibo_mat.append(inner_product(fibo_mat[-1], fibo_mat[-1]))

a = [[1, 0], [0, 1]]
b = [[1, 0], [0, 1]]

for i in range(n.bit_length()):
    if n & (1 << i):
        a = inner_product(a, fibo_mat[i])
for i in range(m.bit_length()):
    if m & (1 << i):
        b = inner_product(b, fibo_mat[i])
ans = b[0][1] - a[0][1]

print(ans if ans >= 0 else (ans + DIVIER))
