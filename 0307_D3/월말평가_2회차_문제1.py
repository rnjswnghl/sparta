# 싸피운동회. 깃발게임 진행.
# 게임은 팀원들 한 줄로 서서 지시에 따라
# 기를 올리거나 내리는 동작, 모든 지시가 끝난 후 
# 정확한 상태가 되었는지 확인
# N명의 팀원으로 구성, 1번부터 N번까지
# 기를 들거나 내린 상태로 대기
# M번의 명령, 각 명령은 정수a, b, c로 구성
# a 난이도, b 기준번호, c 비교 범위 의미
# b번자리에서 거리가 1인 좌우 두 칸의 상태를 비교
# 깃발의 상태가 다르면 유지, 같으면 둘 다 바꾼다.
# 이후 거리가 c인 자리까지 같은 작업 반복

# 첫 줄 팀 수 T
# 다음 줄 N과M
# 다음 줄 빈칸으로 구분된 N명의 초기 상태, 
# 이후M 줄에 걸쳐 a b c

# 테스트 케이스 개수 입력
T = int(input())

# 테스트 케이스 반복
for tc in range(1, T + 1):
    # N: 팀원 수, M: 명령 수
    N, M = map(int, input().split())
    # 팀원들의 초기 상태
    origin = list(map(int, input().split()))

    # 지시 횟수 반복
    for _ in range(M):
        # a: 난이도, b: 기준 번호, c: 비교 범위
        a, b, c = map(int, input().split())
        # b는 1부터 시작하니 인덱스 맞추기 위해 -1
        b -= 1

        # 뒤집어야할 범위 내에서 반복
        for j in range(1, c + 1):
            # 비교할 범위가 올바른지 확인   
            if 0 > b - j or b + j >= N:
                # 올바르지 않으면 멈춤
                break

            else:
                # 비교할 왼쪽과 오른쪽이 같은 상태이면 뒤집기
                if origin[b - j] == origin[b + j]:
                    origin[b - j] = 1 - origin[b - j]
                    origin[b + j] = 1 - origin[b + j]

    # 출력
    print(f'#{tc}', *origin)