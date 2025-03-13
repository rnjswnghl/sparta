# 종이 꽃가루 들어있는 풍선 M개씩 N개의 줄
# 풍선 터뜨리면 1개씩 상하 좌우의 풍선이 추가로 터짐
# N*M개의 풍선에 들어있는 종이 꽃가루 개수 A가 주어지면
# 한 개의 풍선을 택했을 경우 날릴 수 있는 최대 꽃가루의 수

# 첫 줄 테스트 케이스 개수
# 다음 줄 N개의 줄, M의 풍선
# 풍선 안에 든 종이 꽃가루의 개수

# 테스트케이스 개수
T = int(input())

# 델타 : 상, 우, 하, 좌
r = [-1, 0, 1, 0]
c = [0, 1, 0, -1]

# 테스트케이스
for tc in range(1, T + 1):

    # N: 행 개수, M: 열 개수
    N, M = map(int, input().split())

    # NxM 크기의 풍선판 리스트로 저장
    flower = [list(map(int, input().split())) for _ in range(N)]

    # 최대 꽃가루 개수 저장하는 변수
    max_flower = 0

    # 모든 풍선(i, j) 순회
    for i in range(N):
        for j in range(M):

            # 현재 풍선 꽃가루 개수 저장
            total = flower[i][j]

            # 4방향(상, 우, 하, 좌)으로 추가로 터지는 풍선
            for d in range(4):
                # 이동할 행 좌표
                ni = i + r[d]
                # 이동할 열 좌표
                nj = j + c[d]

                # 범위를 벗어나지 않는 경우만 추가 계산
                if 0 <= ni < N and 0 <= nj < M:
                    total += flower[ni][nj]

            # 최대 꽃가루 개수 갱신
            max_flower = max(max_flower, total)

    # 출력
    print(f'#{tc} {max_flower}')
