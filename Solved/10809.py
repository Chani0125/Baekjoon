word = list(input())
alpha = []

for i in range(26):
    alpha.append(-1)

for i, c in enumerate(word):
    idx = ord(c)-97
    if alpha[idx] == -1:
        alpha[idx] = i

for i in alpha:
    print(i, end=" ")
