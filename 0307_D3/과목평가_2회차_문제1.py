# 싸피운동회. 깃발게임이진행.
# 게임은 팀원들 한 줄로 서서 지시에 따라
# 기를 올리거나 내리는 동작, 모든 지시가 끝난 후 
# 정확한 상태가 되었는지 확인
# N명의팀원으로구성, 1번부터N번까지
# 기를 들거나 내린 상태로 대기
# M번의 명령, 각 명령은 정수a, b, c로 구성
# a 난이도, b 기준번호, c 사람 수 의미

# 첫 줄 팀 수 T
# 다음 줄 N과M
# 다음 줄 빈칸으로 구분된 N명의 초기 상태, 
# 이후M 줄에 걸쳐 a b c

# 팀 수
T = int(input())

# 반복
for tc in range(1, T+1):
    # 팀원 수 N, 지시 반복 횟수 M
    N, M = map(int, input().split())
    # 팀 깃발 초기 상태
    origin = list(map(int, input().split()))

    # 지시 횟수 반복
    for _ in range(M):
        # 난이도 a, 기준번호 b, 사람 수 c
        a, b, c = map(int, input().split())
        # 인덱스 번호 맞추기
        b -= 1

        for i in range(b, b+c):
            if 0 < i <= N:
                origin[i] = 1 - origin[i]

    print(f'#{tc}', *origin)