for _ in range(3):
    h1, m1, s1, h2, m2, s2 = map(int, input().split())
    s = h1 * 3600 + m1 * 60 + s1
    e = h2 * 3600 + m2 * 60 + s2
    t = e - s
    h = t // 3600
    m = t % 3600 // 60
    s = t % 60
    print(h, m, s)
    