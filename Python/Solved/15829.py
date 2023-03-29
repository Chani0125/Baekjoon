l = int(input())
s = input()
h = 0
for idx, letter in enumerate(s):
    h += (ord(letter) - 96) * (31 ** idx)
h %= 1234567891
print(h)
