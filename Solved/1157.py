word = list(input())
word_count = []

for i in range(0, 26):
    word_count.append(word.count(chr(i+65)))
    word_count[i] += word.count(chr(i+97))

if not word_count.count(max(word_count)) == 1:
    print("?")
else:
    ans = chr(word_count.index(max(word_count))+65)
    print(ans)
