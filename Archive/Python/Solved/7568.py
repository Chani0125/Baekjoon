N = int(input())
people = []
rank = []
for i in range(N):
    weight, height = map(int, input().split())
    people.append((weight, height))
    rank.append(0)

for i in range(N):
    for j in range(N):
        if not i == j:
            if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
                rank[i] += 1

for i in rank:
    print(i+1, end=" ")

# rank_set = list(set(rank))
# rank_delay = 0
# rank_order = []
# for i in range(len(rank_set)):
#     rank_order.append(1 + i + rank_delay)
#     rank_delay += rank.count(rank_set[i]) - 1
#
# print(rank)
# print(rank_set, rank_order)
#
# for i in rank:
#     print(rank_order[rank_set.index(i)], end=" ")
