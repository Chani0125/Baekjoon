import sys

def lcs(str1, str2):
    pass

str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()
dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]



print(*dp, sep='\n')
print(lcs(str1, str2))

