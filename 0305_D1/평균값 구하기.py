# 10개의 수 입력 받아 평균값 출력하기
# 소수점 첫째 자리에서 반올림한 정수 출력
# 첫 줄은 테스트 케이스
# 테스트 케이스 10개의 수

# 테스트 케이스의 개수 입력 받기
T = int(input())

# 테스트 케이스 개수 만큼 반복
for tc in range(1, T+1):
    # 테스트 케이스 숫자 리스트 형태로 입력 받기
    N = list(map(int, input().split()))
    # 입력 받은 수의 평균 구하기
    an = sum(N) / len(N)
    # 테스트 케이스 번호와 소수점 첫째자리에서 반올림한 정수 출력
    print(f'#{tc} {round(an)}')