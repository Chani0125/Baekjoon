import math
import sys

n = int(sys.stdin.readline().strip())
a = n

while a % 4 == 0:
    a //= 4
if a >= 7 and (a - 7) % 8 == 0:
    print(4)
else:
    root = int(math.sqrt(n))
    if n == root ** 2:
        print(1)
    else:
        is_find = False
        for i in range(1, root + 1):
            for j in range(1, root + 1):
                if i ** 2 + j ** 2 == n:
                    print(2)
                    is_find = True
                    break
            if is_find:
                break
        else:
            print(3)
