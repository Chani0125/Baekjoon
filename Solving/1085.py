x, y, w, h = map(int, input().split())
d = [w-x, x, h-y, y]
print(min(d))