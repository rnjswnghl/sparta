# N = 2^a x 3^b x 5^c x 7^d x 11^e
# N이 주워질 때 a, b, c, d, e 출력하기

# 첫 줄은 테스트 케이스의 수
# 각 테스트 케이스

# 테스트 케이스 개수
T = int(input())

# 테스트 케이스 반복
for tc in range(1, T + 1):
    # N : 인수분해할 수
    N = int(input())
    # div : 인수들
    div = [2, 3, 5, 7, 11]
    # 인수들의 출현 수를 저장할 인수들 만큼의 리스트 생성
    cnt = [0] * len(div)

    #  인수들의 수만큼 반복
    for i in range(len(div)):
        # N을 인수로 나눌 수 있다면 계속 반복
        while N % div[i] == 0:
            # N을 i 인수로 나누기
            N //= div[i]
            # 나눠지면 해당 i에 +1
            cnt[i] += 1
            
    # 결과 출력
    print(f'#{tc}', *cnt)
