l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

p = divmod(a, c)
q = divmod(b, d)

x = p[0] + (p[1] > 0)
y = q[0] + (q[1] > 0)

print(l - max(x, y))