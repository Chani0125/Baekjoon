std = set(range(1, 31))
for _ in range(28):
    std.remove(int(input()))
print("\n".join(list(map(str, std))))
