word = list(input())
words = set()
for i in range(len(word)):
    for j in range(len(word)-i):
        words.add("".join(word[j:j+i+1]))
print(len(words))