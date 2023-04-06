import sys
from collections import deque

n = int(sys.stdin.readline())
stack = deque()
if n % 2 == 0:
    stack.append(([n // 2, n // 2 - 1, n // 2 + 1], 0))
else:
    stack.append(([n // 2 + 1, n // 2], 1))

# f(n)
# = f(n-1) * 1 + f(n-2) * 1 = f(n-1) * f(2) + f(n-2) * f(1)
# = f(n-2) * 2 + f(n-3) * 1 = f(n-2) * f(3) + f(n-3) * f(2)
# = f(n-3) * 3 + f(n-4) * 2 = f(n-3) * f(4) + f(n-4) * f(3)
# = f(n-4) * 5 + f(n-5) * 3 = f(n-4) * f(5) + f(n-5) * f(4)
# = f(n-5) * 8 + f(n-6) * 5 = f(n-5) * f(6) + f(n-6) * f(5)
# = f(n-k) * f(k+1) + f(n-(k+1)) * f(k)

# f(9)
# = f(5) * f(5) + f(4) * f(4)
# = f(6) * f(4) + f(5) * f(3)

# f(2n-1)
# = f(n) * f(n) + f(n-1) * f(n-1)

# f(2n)
# = f(n) * f(n+1) + f(n) * f(n-1)
# = f(n) * (f(n-1) + f(n+1))
	