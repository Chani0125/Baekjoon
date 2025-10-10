import sys

f = sys.stdin.readlines()

for t in range(len(f)//32):
    pc, s = 0, 0
    mem = [int(i[:8], base=2) for i in f[t*32:(t+1)*32]]

    while True:
        opt, opr = mem[pc] // 32, mem[pc] % 32
        pc += 1
        if pc > 31: pc -= 32
        
        if opt == 0:
            mem[opr] = s
        elif opt == 1:
            s = mem[opr]
        elif opt == 2:
            if s == 0:
                pc = opr
        elif opt == 3:
            pass
        elif opt == 4:
            s -= 1
            if s < 0:
                s += 256
        elif opt == 5:
            s += 1
            if s > 255:
                s -= 256
        elif opt == 6:
            pc = opr
        else:
            break

    ans = bin(s)[2:]
    print('0'*(8-len(ans)) + ans)