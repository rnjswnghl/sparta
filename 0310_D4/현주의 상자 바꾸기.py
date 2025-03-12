# 1번부터 N번까지 N개의 상자
# 초기 상태는 모두 0
# Q회 동안 일정 범위의 연속한 상자를 동일한 숫자로 변경
# i번째 작업에 대해 L번 부터 R번 상자까지의 값을 i로 변경
# 작업 완료 후 적혀있는 상자들의 값 출력

# 첫 줄 테스트 케이스의 개수
# 다음 줄 두 정수 N, Q 공백으로 구분
# 다음 줄 Q개의 줄에 걸쳐 L, R 입력

# 테스트 케이스 개수 입력
T = int(input())

# 테스트 케이스 반복
for tc in range(1, T + 1):
    # 상자의 개수 N, 작업 횟수 Q
    N, Q = map(int, input().split())
    # 초기 상자 상태 (모두 0으로 초기화)
    boxes = [0] * N

    # i는 현재 작업 번호 (1부터 시작)
    for i in range(1, Q + 1):
        # 변경할 범위 L ~ R
        L, R = map(int, input().split())

        # L-1부터 R까지 반복 (0-based index)
        for k in range(L - 1, R):
            # i번째 작업 번호를 상자에 기록
            boxes[k] = i

    # 결과 출력
    print(f"#{tc}", *boxes)
