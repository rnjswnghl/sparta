# N개의 0과 1로 이루어진 수열에서 연속한 1의 개수 중 최대값을 출력하는 프로그램
# 입력
# 첫 줄에 테스트케이스 개수 T
# 다음 줄 수열의 길이 N,
# 다음 줄에 N개의 0과1로 구성된 수열 공백없이 제공
# 1<=T<=10, 10<=N<=1000

# 테스트 케이스 개수
T = int(input())

# 테스트 케이스 반복
for tc in range(1, T+1):
    # 수열의 길이 N
    N = int(input())
    # 공백없이 입력
    arr = list(map(int, input().strip()))
    # 최대값
    max_cnt = 0
    # 연속하는 수
    cnt = 0

    # 수열의 수만큼 반복
   for i in range(N):
       # 수열 안에 있는 i번째 수가 1이면 
        if arr[i] == 1:
            # 횟수 +1
            cnt += 1
            # 최댓값 갱신
            max_cnt = max(max_cnt, cnt)

        else:
            # 연속하지 않으면 초기화
            cnt = 0
    
    # 출력
    print(f'#{tc} {max_cnt}')
