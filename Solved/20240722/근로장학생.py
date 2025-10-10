import sys

input = sys.stdin.readline
n, m = map(int, input().split())
dic = {}
for _ in range(n):
    a, b = input().split()
    dic[a] = b

for _ in range(m):
    flag = False
    s = input().strip()
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if s[i:j] in dic:
                print(dic[s[i:j]], end='')
                flag = True
    if not flag:
        print(-1, end='')
    print()