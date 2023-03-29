import sys


def sugang(i, total_k, k):
    if i >= len(lectures):
        return 0
    for h in range(lectures[i][1]-1, lectures[i][2]):
        if time_table[lectures[i][0]-1][h]:
            return sugang(i+1, total_k, k)
    else:
        if total_k + lectures[i][3] == k:
            return 1 + sugang(i+1, total_k, k)
        elif total_k + lectures[i][3] > k:
            return sugang(i+1, total_k, k)
        else:
            for h in range(lectures[i][1] - 1, lectures[i][2]):
                time_table[lectures[i][0] - 1][h] = True
            ans = sugang(i+1, total_k + lectures[i][3], k)
            for h in range(lectures[i][1] - 1, lectures[i][2]):
                time_table[lectures[i][0] - 1][h] = False
            return ans + sugang(i+1, total_k, k)


n, k = map(int, sys.stdin.readline().split())
lec = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]


time_table = [[False, ] * 10 for _ in range(5)]

lectures = []
for idx, (w, s, e) in enumerate(lec):
    if w != 5:
        lectures.append((w, s, e, e - s + 1))

print(sugang(0, 0, k))
