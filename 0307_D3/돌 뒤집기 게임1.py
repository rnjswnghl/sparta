# 돌 양면 각각 흰색과 검은색
# 뒤집기는 i번째부터 j개의 돌을 i번째 돌의 색으로 변경
# 뒤집기는 가능한 돌만 진행

# 첫 줄 게임의 수 T
# 다음 줄 N개의 돌, 뒤집기 반복 횟수 M
# 다음 줄 돌의 초기 상태 origin
# 다음 줄 i번부터, j번까지

# 테스트 케이스 개수
T = int(input())

# 케스트 케이스 반복
for tc in range(1, T+1):
    # 돌의 개수와 뒤집을 횟수 입력
    N, M = map(int, input().split())
    # 돌의 초기 상태
    origin = list(map(int, input().split()))

    # 뒤집는 횟수만큼 반복
    for _ in range(M):
        # 뒤집을 곳에서부터 몇개 뒤집을지 입력
        s, e = map(int, input().split())

        # 뒤집는 곳은 1부터 시작하지만 인덱스는 0부터 시작하니 -1
        s = s - 1

        # 뒤집는 곳에서 부터 뒤집어질 돌의 위치까지 반복
        for i in range(s, s+e):
            # 만약 뒤집는 곳의 위치가 돌의 개수보다 작으면(범위 초과 방지)
            if i < N:
                # 시작 돌이 0이면
                if origin[s] == 0:
                    # 1번째 돌도 같은걸로 맞추기
                    origin[i] = 0
                # 시작돌이 1일 경우
                elif origin[s] == 1:
                    origin[i] = 1

    # 출력
    print(f"#{tc}",*origin)