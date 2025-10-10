import sys

string = sys.stdin.readline().strip()
while string != '#':
    ans = 0
    for i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        ans += string.count(i)
    print(ans)
    string = sys.stdin.readline().strip()