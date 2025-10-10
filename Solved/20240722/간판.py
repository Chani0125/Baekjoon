import sys

input = sys.stdin.readline

n = int(input())
ans = 0
name = input().strip()

for _ in range(n):
    s = input().strip()
    for i in range(len(s)):
        if s[i] == name[0]:
            for j in range(i+1, len(s)):
                if s[j] == name[1]:
                    for k in range(2, len(name)):
                        if i + k * (j - i) >= len(s):
                            break
                        if s[i + k * (j - i)] != name[k]:
                            break
                    else:
                        ans += 1
                        break
            else:
                continue
            break
                
print(ans)