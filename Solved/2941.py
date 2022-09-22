word = input()
a = 0
two_word = ("c=", "c-", "d-", "lj", "nj", "s=", "z=")

for i in two_word:
    a += word.count(i)

print(len(word) - a - word.count("dz="))
