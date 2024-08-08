n = int(input())

fibo_mat = [[[1, 1], [1, 0]]]

DIVIER = 1000000

def inner_product(mat1, mat2):
    a = (mat1[0][0] * mat2[0][0] + mat1[0][1] * mat2[1][0]) % DIVIER
    b = (mat1[0][0] * mat2[0][1] + mat1[0][1] * mat2[1][1]) % DIVIER
    c = (mat1[1][0] * mat2[0][0] + mat1[1][1] * mat2[1][0]) % DIVIER
    d = (mat1[1][0] * mat2[0][1] + mat1[1][1] * mat2[1][1]) % DIVIER
    return [[a, b], [c, d]]

for i in range(n.bit_length()):
    fibo_mat.append(inner_product(fibo_mat[-1], fibo_mat[-1]))

ans = [[1, 0], [0, 1]]

for i in range(n.bit_length()):
    if n & (1 << i):
        ans = inner_product(ans, fibo_mat[i])

print(ans[0][1])