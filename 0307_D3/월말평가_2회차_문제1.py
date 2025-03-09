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

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())  # N: 팀원 수, M: 명령 수
    origin = list(map(int, input().split()))  # 팀원들의 초기 상태

    for _ in range(M):
        a, b, c = map(int, input().split())  # a: 난이도, b: 기준 번호, c: 비교 범위
        b -= 1  # b는 1-based index로 주어지므로 0-based index로 변경

        # 비교할 범위가 올바른지 확인
        for i in range(max(0, b - c), min(N, b + c + 1)):  # 범위 내에서 비교
            if i != b and i - 1 >= 0 and i + 1 < N:  # i-1, i+1이 배열 범위 내에 있을 때만 비교
                if origin[i-1] == origin[i+1]:
                    origin[i-1] = 1 - origin[i+1]
                    origin[i+1] = 1 - origin[i-1]
    
    print(f'#{tc}', *origin)

                    