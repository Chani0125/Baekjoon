a, p1 = map(int, input().split())
r, p2 = map(int, input().split())

if a * p2 > r**2 * 3.14159265358979 * p1:
    print("Slice of pizza")
else:
    print("Whole pizza")