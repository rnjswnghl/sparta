T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    # 농장 정보
    field = [list(map(int, input())) for _ in range(N)]

    # 수익
    crops = 0

    # 농장의 정중앙과 거리 차이가 d 이하인 곳만 수확할수 있다.
    # 거리 d는 농장의 한 변의 길이 // 2
    d = N // 2

    # 정 중앙의 좌표
    center = (d, d)

    # 모든 위치 (r,c) 에서 정중앙까지 이동하는데 가로로 이동한 횟수 x, 세로로 이동한 횟수 y
    # x + y <= d 이하인 곳들의 합을 구한다.
    # 가로로 이동한 횟수 => (r,c) 와 (d,d) 에서 c, d의 차이의 절댓값
    # 세로로 이동한 횟수 => (r,c) 와 (d,d) 에서 r, d의 차이의 절댓값
    for r in range(N):
        for c in range(N):
            # 거리 계산
            if abs(r-d) + abs(c-d) <= d:
                crops += field[r][c]

    print(f"#{tc} {crops}")
