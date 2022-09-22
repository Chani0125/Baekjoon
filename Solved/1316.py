def cal_group_word(c):
    word_list = sorted(list(c))
    sorted_word = ""

    for i in word_list:
        sorted_word += i

    for i in range(97, 123):
        re_word = chr(i) * word_list.count(chr(i))
        if re_word not in c:
            return 0

    return 1


n = int(input())
word = [input() for i in range(n)]
count = 0

for i in word:
    count += cal_group_word(i)

print(count)
