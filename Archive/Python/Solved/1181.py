N = int(input())
word = [input() for i in range(N)]
word.sort(key=lambda x:(len(x), x))
now = None
for i in word:
    if now == i:
        continue
    else:
        now = i
        print(i)
