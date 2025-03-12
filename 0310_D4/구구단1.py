# 정수 N이 주어졌을 때, 
# N이 1 이상 9 이하의 두 수 a, b의 곱으로 표현 가능한지 판단.

# 첫째 줄 테스트 케이스의 수 tc
# 다음 줄 하나의 정수 N
# 표현 가능하면 "Yes", 아니면 "No"

# 테스트 케이스 개수
T = int(input())

# 테스트 케이스
for tc in range(1, T+1):
    # 정수
    N = int(input())
    # 결과의 초기값은 부정으로!
    result = "No"

    # 1에서 9까지의 수 반복. a = i
    for i in range(1, 10):
        # 1에서 9까지의 수 반복. b = i
        for j in range(1, 10):

            # 두 수의 곱이 정수와 같으면
            if i * j == N:
                # Yes 출력과 반복 중지
                result = "Yes"
                break
            # 정수를 표현 못 하면 No 출력
            else:
                result = "No"

        # 결과 값이 Yes면 반복 그만
        if result == "Yes":
            break
    
    # 출력
    print(f'#{tc}', result)