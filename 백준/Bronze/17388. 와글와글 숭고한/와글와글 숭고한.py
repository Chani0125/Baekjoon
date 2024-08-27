a = list(map(int, input().split()))
if sum(a) >= 100:
    print('OK')
else:
    b = a.index(min(a))
    print(['Soongsil', 'Korea', 'Hanyang'][b])