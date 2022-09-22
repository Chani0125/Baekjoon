n = int(input())

for i in range(n):
    r, word = input().split()
    word_list = list(word)
    for j in word_list:
        for k in range(int(r)):
            print(j, end="")
    print()
