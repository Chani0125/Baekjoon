n, m = map(int, input().split())
a = [input().strip() for _ in range(n)]
print(*map(lambda x: x[::-1], a), sep='\n')