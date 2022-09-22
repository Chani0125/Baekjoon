def find_prime_number(end):
    list_prime_idx = [False, False] + [True, ] * (end - 1)
    for i in range(2, end + 1):
        if i * i > end:
            break
        if not list_prime_idx[i]:
            continue
        for j in range(i * 2, end + 1, i):
            list_prime_idx[j] = False
    list_prime_num = []
    for idx, val in enumerate(list_prime_idx):
        if val:
            list_prime_num.append(idx)
    return list_prime_num


def find_prime_factor(end):
    list_prime_idx = [True, ] * end
    for i in range(1, end):
        if (i+1) * (i+1) > end:
            break
        if not list_prime_idx[i]:
            continue
        for j in range((i+1) * 2 - 1, end, i+1):
            list_prime_idx[j] = False
    list_prime_num = []
    for idx, val in enumerate(list_prime_idx):
        if val:
            list_prime_num.append(idx+1)
    return list_prime_num
