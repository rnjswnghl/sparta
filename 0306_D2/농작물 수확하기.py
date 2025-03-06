# N * N 크기의 농장
# 이상한 규칙 있음!
# 1. 농장의 크기는 항상 홀수
# 2. 수확은 항상 농장의 크기에 딱 맞는 정사각형 마름모 형태만 가능
# 농작물의 크기 N과 가치 주어짐, 얻을 수 있는 수익?

# 첫 줄 테스트 케이스의 개수
# 다음 줄 농장의 크기 N
# 다음 농장 내 농작물의 가치

# 테스트 케이스 개수 입력
T = int(input())

# 테스트 케이스 반복
for tc in range(1, T + 1):
    # N : 농장의 크기
    N = int(input())
    # area : 농장의 가치
    area = [list(map(int, input())) for _ in range(N)]
    # mid : 중앙 인덱스 값
    mid = N // 2
    # K : 좌우로 확장할 크기
    K = 0
    # pro : 농장 내 가치를 합한 이익
    pro = 0

    # 농장의 크기만큼 반복
    for i in range(N):
        # 시작점 = 중앙에서 K 뺀 만큼의 위치(왼쪽으로 확장)
        start = mid - K
        # 끝점  = 중앙에서 K만큼 더한 위치(오른쪽으로 확장)
        end = mid + K + 1  
        # area의 i행에서 시작점에서 끝점까지의 수 더해서 저장하기
        pro += sum(area[i][start:end])

        # N*N 크기의 배열이라 mid는 행과 열의 중앙!
        # 따라서 i번째 행이 mid보다 작으면
        if i < mid:
            # 범위 확장
            K += 1
        else: 
            # 중앙 이후부터는 범위 축소
            K -= 1

    print(f'#{tc} {pro}')
        
