# 우주선 싸피2호 화성에 착륙해 주변 사진 찍어 전송
# 착륙 지점을 중심으로 주변 8개 구역 대상으로
# 착륙 지점보다 높이가 낮은 구역의 사진 촬영
# 

# # 8방향 (상, 하, 좌, 우, 대각선)
# DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1),
#               (0, -1),         (0, 1),
#               (1, -1), (1, 0), (1, 1)]

# def count_landing_sites(N, grid):
#     count = 0  # 착륙 가능한 위치 개수

#     for r in range(N):
#         for c in range(N):
#             current_height = grid[r][c]
#             lower_or_equal_count = 0  # 현재보다 낮거나 같은 칸 개수

#             for dr, dc in DIRECTIONS:
#                 nr, nc = r + dr, c + dc
#                 if 0 <= nr < N and 0 <= nc < N:  # 범위 확인
#                     if grid[nr][nc] <= current_height:
#                         lower_or_equal_count += 1
            
#             if lower_or_equal_count >= 4:  # 조건 충족
#                 count += 1

#     return count

# # 입력 처리
# T = int(input())  # 테스트 케이스 개수
# for test_case in range(1, T + 1):
#     N = int(input())  # 배열 크기
#     grid = [list(map(int, input().split())) for _ in range(N)]  # N x N 격자 입력

#     result = count_landing_sites(N, grid)
#     print(f"#{test_case} {result}")


# 8방향 탐색 (상, 하, 좌, 우, 대각선)
DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),         (0, 1),
              (1, -1), (1, 0), (1, 1)]
 
# 입력 처리
T = int(input())  # 테스트 케이스 개수
for test_case in range(1, T + 1):
    N, M = map(int, input().split())  # 지형 크기
    grid = [list(map(int, input().split())) for _ in range(N)]  # 높이 정보
 
    count = 0  # 예비 후보지 개수
 
    for r in range(N):
        for c in range(M):
            current_height = grid[r][c]
            lower_count = 0  # 착륙지보다 낮은 구역 개수
 
            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < M:  # 범위 체크
                    if grid[nr][nc] < current_height:
                        lower_count += 1
 
            if lower_count >= 4:  # 조건 충족
                count += 1
 
    print(f"#{test_case} {count}")