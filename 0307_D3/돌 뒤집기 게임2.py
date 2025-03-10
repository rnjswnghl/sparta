# i번째 돌을 사이에 두고 마주보는 j개의 돌에 대해
# 각각 같은 색이면 뒤집고, 다른 색이면 그대로 둔다.
# 주어진 돌을 벗어나는 경우 뒤집기 중지

# 게임의 개수 T
# 돌의 수 N, 뒤집기 횟수 M
# 돌의 초기 상태 origin
# 기준 돌 i, 마주보는 돌 개수 j

# 테스트 케이스 개수 입력
T = int(input())

# 테스트 케이스 반복
for tc in range(1, T+1):
    # 돌의 수, 뒤집을 횟수 입력
    N, M = map(int, input().split())
    # 돌의 초기 상태
    origin = list(map(int, input().split()))

    # 돌 뒤집는 횟수 반복
    for _ in range(M):
        # 기준 돌의 위치와 기준에서 확인할 돌 개수
        i, j = map(int, input().split())
        # 인덱스 맞추기
        i -= 1

        # 1부터 시작해서 돌 뒤집는 범위까지 반복
        for k in range(1, j+1):
            # 범위 확인
            if i - k < 0 or i + k >= N:
                # 벗어나면 멈춤
                break
            else:
                # 왼쪽이랑 오른쪽 돌 같으면 뒤집기
                if origin[i-k] == origin[i+k]:
                    origin[i-k] = 1 - origin[i-k]
                    origin[i+k] = 1 - origin[i+k]

    # 출력
    print(f'#{tc}',*origin)