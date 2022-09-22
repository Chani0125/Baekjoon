word = list(input())
t = 0

for i in word:
    a = ord(i) - 56
    if a >= 27:
        a -= 1
        if a == 33:
            a -= 1
    t += a // 3

print(t)
