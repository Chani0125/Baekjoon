# T: 테스트 케이스의 개수
T = int(input())

for t in range(T):
    # N: 마을에 있는 집의 개수, M: 도둑이 돈을 훔칠 연속된 집의 개수, K: 자동 방범 장치가 작동하는 최소 돈의 양
    N, M, K = map(int, input().split())
    money = list(map(int, input().split()))

    if N == M:
        if sum(money) < K:
            cnt = 1
        else:
            cnt = 0
    else:
        money += money[:M - 1:]
        cnt = 0
        val = sum(money[0:M])
        for i in range(N-1):
            if val < K:
                cnt += 1
            val += money[i + M] - money[i]
        else:
            if val < K:
                cnt += 1

    print(cnt)
