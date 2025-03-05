# N 개의 숫자로 구성된 숫자열 Ai (i=1~N) 
# M 개의 숫자로 구성된 숫자열 Bj (j=1~M)
# Ai, Bj 움직여 숫자들 서로 마주보는 위치를 변경 가능
# 단, 더 긴 쪽의 양끝을 벗어나서는 안 됨
# 서로 마주보는 숫자들을 곱한 뒤 모두 더할 때 최댓값을 구하라.

# 첫 줄에는 테스트 케이스의 개수 T
# 다음 줄에 N 과 M
# Aj
# Bj

# 테스트 케이스 개수
T = int(input())

# 테스트 케이스 반복
for tc in range(1, T+1):
    # N : Aj열 구성 개수, M : Bj열 구성 개수
    N, M = map(int, input().split())
    # A : Aj열
    A = list(map(int, input().split()))
    # B : Bj열
    B = list(map(int, input().split()))
    # 최댓값 초기화
    max_sum = 0

    # N과 M의 개수 비교 해서 N이 더 크면 Aj열과 Bj열, N과 M 서로 위치 변경. N과 A는 항상 작은 값
    if N > M:
        N, M = M, N
        A, B = B, A

        for sums in range(M-N+1):
            ex_sum = 0
            for i in range(N):
                ex_sum += A[i] * B[i+sums]

        if ex_sum > max_sum:
            max_sum = ex_sum

    print(f'#{tc} {max_sum}')