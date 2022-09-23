# T: 테스트 케이스의 개수
T = int(input())

for t in range(T):
    # N: 마을에 있는 집의 개수, M: 도둑이 돈을 훔칠 연속된 집의 개수, K: 자동 방범 장치가 작동하는 최소 돈의 양
    N, M, K = map(int, input().split())

    # 집에서 각각 보관중인 돈의 양 입력
    money = list(map(int, input().split()))
    money += money[:M-1:]
    cnt = 0

    for i in range(N):
        val = 0
        for j in money[i:i+M]:
            val += j
        if val < K:
            cnt += 1

    print(cnt)
