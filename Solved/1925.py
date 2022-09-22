# 3개의 점 입력
p = []
for i in range(3):
    x, y = map(int, input().split())
    p.append((x, y))

m11 = p[0][0] - p[1][0]  # 직선 AB의 X 변화
m12 = p[0][1] - p[1][1]  # 직선 AB의 Y 변화
m21 = p[1][0] - p[2][0]  # 직선 BC의 X 변화
m22 = p[1][1] - p[2][1]  # 직선 BC의 Y 변화

ab2 = m11 ** 2 + m12 ** 2  # 선분 AB ^ 2
bc2 = m21 ** 2 + m22 ** 2  # 선분 BC ^ 2
ca2 = (p[2][0] - p[0][0]) ** 2 + (p[2][1] - p[0][1]) ** 2  # 선분 CA ^ 2
len2 = sorted([ab2, bc2, ca2])

if m11 * m22 == m12 * m21:  # 직선 AB 기울기 == 직선 BC의 기울기
    print("X")
elif len2[0] == len2[2]:
    print("JungTriangle")
elif len2[0] == len2[1] or len2[1] == len2[2]:
    if len2[2] > len2[0] + len2[1]:
        print("Dunkak2Triangle")
    elif len2[2] == len2[0] + len2[1]:
        print("Jikkak2Triangle")
    else:
        print("Yeahkak2Triangle")
else:
    if len2[2] > len2[0] + len2[1]:
        print("DunkakTriangle")
    elif len2[2] == len2[0] + len2[1]:
        print("JikkakTriangle")
    else:
        print("YeahkakTriangle")
