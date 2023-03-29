n = int(input())
for i in range(n):
    score_list = list(map(int, input().split()))
    score = sum(score_list[1:]) / score_list[0]
    num = 0
    for j in score_list[1:]:
        if score < j:
            num += 1
    ratio = num / len(score_list[1:])
    print(f"{ratio:.3%}")
