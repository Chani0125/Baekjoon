n = int(input())

v = [0]
for i in range(1, 33):
    v.append(9 * (10 ** ((i-1) // 2)))

now, p = 0, 1
while n > now + (v[p] * p):
    now += v[p] * p
    p += 1

print(now, p)

a = []
q = 1

# while n > now + (p * q * (10 ** ((p-1) // 2 - 1))):
#     now += p * q * (10 ** ((p-1) // 2 - 1))
#     q += 1

# print(now, p, q)


# for i in range(1, (p + 1) // 2):
    
#     while n > now + 



# print(now, p)
# print(v[p] * p)

# (8)8