# 10개의 수 입력 받아, 그 중 홀수만 더한 값 출력하기
# 첫 줄 테스트 케이스의 개수
# 다음 줄 각 테스트 케이스

# 테스트 케이스의 수 입력 받기
T = int(input())

# 테스트 케이스의 수만큼 반복
for tc in range(1, T+1):
    # 테스트 케이스 숫자 입력 받기
    N = list(map(int, input().split()))
    # 홀수 담을 변수 설정
    odd = []

    # 테스트 케이스의 수만큼 반복
    for i in range(len(N)):
        # N의 수가 홀수라면
        if N[i] % 2 != 0:
            # odd에 추가
            odd.append(N[i])
            

    # 테스트 케이스 번호와 홀수의 합 출력하기
    print(f'#{tc} {sum(odd)}')
