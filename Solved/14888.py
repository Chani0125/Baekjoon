def calculate(a, ans, result, idx, plus, minus, multi, divide):
    if plus + minus + multi + divide == 0:
        ans.append(result)
        return True
    if plus > 0:
        calculate(a, ans, result + a[idx], idx+1, plus-1, minus, multi, divide)
    if minus > 0:
        calculate(a, ans, result - a[idx], idx+1, plus, minus-1, multi, divide)
    if multi > 0:
        calculate(a, ans, result * a[idx], idx+1, plus, minus, multi-1, divide)
    if divide > 0:
        if result < 0:
            result = -1 * result // a[idx] * -1
        else:
            result //= a[idx]
        calculate(a, ans, result, idx+1, plus, minus, multi, divide-1)
    return True


n = int(input())
a = list(map(int, input().split()))
o = list(map(int, input().split()))
ans = []
calculate(a, ans, a[0], 1, o[0], o[1], o[2], o[3])
print(max(ans))
print(min(ans))
