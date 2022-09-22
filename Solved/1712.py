A, B, C = map(int, input().split())
if B < C:
    break_even_point = int(A / (C-B) + 1)
    print(break_even_point)
else:
    print(-1)
