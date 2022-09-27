import sys


N = int(sys.stdin.readline())
member = []
for i in range(N):
    age, name = sys.stdin.readline().split()
    member.append((int(age), name, i))
member.sort(key=lambda x:(x[0], x[2]))
for age, name, order in member:
    print(age, name)