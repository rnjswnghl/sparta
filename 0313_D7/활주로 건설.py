# N*N 크기의 절벽지대에 활주로 건설
# 가로 또는 세로 방향으로 건설
# 활주로는 높이가 동일한 구간에서 건설 가능
# 경사로는 길이가 X, 높이는 1
# 경사로는 높이 차이가 1이고 낮은 지형의 높이가 동일하게 경사로의 길이만큼 연속되는 곳에 설치 가능

# 첫 줄 총 테스트 케이스의 개수
# 다음 줄 지도의 크기 N, 경사로의 길이 X
# N개의 줄에 N*N 지형의 정보

# 테스트 케이스 개수
T = int(input())

# 테스트 케이스 반복
for test_case in range(1, T + 1):
    # 지도 크기 N, 경사로 길이 X
    N, X = map(int, input().split())
    # 지형 정보
    area = [list(map(int, input().split())) for _ in range(N)]
    # 활주로 개수
    count = 0

    # 가로 방향(행) 검사
    for i in range(N):
        # 경사로 설치 여부
        installed = [False] * N
        # 활주로 가능 여부
        valid = True

        for j in range(N - 1):
            # 가로로 인접한 두 셀의 높이가 같으면 진행
            if area[i][j] == area[i][j + 1]:
                continue

            # 현재위치+1의 값과 다음 위치의 값이 같으면 높이 차이는 1로 경사로 설치 가능!
            elif area[i][j] + 1 == area[i][j + 1]:
                # 범위 초과하는지 확인
                if j - X + 1 < 0:
                    valid = False
                    break
                # 초과하지 않고 진행시
                for k in range(j - X + 1, j + 1):
                    # 현재 위치의 높이와 옆의 위치의 높이가 같지 않거나 이미 그 자리에 설치되어있는 경우
                    if area[i][k] != area[i][j] or installed[k]:
                        valid = False
                        break
                    # 경사로 설치
                    installed[k] = True

            # 현재 위치에서 옆 위치의 값과 1 차이 나는 경우
            elif area[i][j] - 1 == area[i][j + 1]:
                # 범위 초과
                if j + X >= N:
                    valid = False
                    break
                for k in range(j + 1, j + X + 1):
                    # 현재 위치의 높이와 옆의 위치의 높이가 같지 않거나 이미 그 자리에 설치되어있는 경우
                    if area[i][k] != area[i][j + 1] or installed[k]:
                        valid = False
                        break
                    # 경사로 설치
                    installed[k] = True

            else:  # 높이 차이가 2 이상이면 활주로 불가
                valid = False
                break

        if valid:
            count += 1

    # 세로 방향(열) 검사
    for j in range(N):
        installed = [False] * N  # 경사로 설치 여부
        valid = True  # 활주로 가능 여부

        for i in range(N - 1):
            if area[i][j] == area[i + 1][j]:  # 높이 같으면 진행
                continue
            elif area[i][j] + 1 == area[i + 1][j]:  # 오르막
                if i - X + 1 < 0:  # 범위 초과
                    valid = False
                    break
                for k in range(i - X + 1, i + 1):
                    if (
                        area[k][j] != area[i][j] or installed[k]
                    ):  # 높이 다르거나 이미 설치됨
                        valid = False
                        break
                    installed[k] = True  # 경사로 설치
            elif area[i][j] - 1 == area[i + 1][j]:  # 내리막
                if i + X >= N:  # 범위 초과
                    valid = False
                    break
                for k in range(i + 1, i + X + 1):
                    if (
                        area[k][j] != area[i + 1][j] or installed[k]
                    ):  # 높이 다르거나 이미 설치됨
                        valid = False
                        break
                    installed[k] = True  # 경사로 설치
            else:  # 높이 차이가 2 이상이면 활주로 불가
                valid = False
                break

        if valid:
            count += 1

    print(f"#{test_case} {count}")  # 결과 출력
