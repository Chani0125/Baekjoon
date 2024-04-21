import sys

c = int(sys.stdin.readline().strip())
for _ in range(5):
    n = list(map(int, sys.stdin.readline().split()))
    avg = sum(n[1:]) // n[0]
    ans = 0
    for s in n[1:]:
        if s > avg:
            ans += 1
    ans /= n[0]
    print(f'{round(ans*100, 3):02.3f}%')
