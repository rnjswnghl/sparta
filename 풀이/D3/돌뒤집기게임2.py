T = int(input())

for tc in range(1, T+1):
    # N : 돌의 개수
    # M : 뒤집기를 진행하는 횟수
    N, M = map(int, input().split())

    # 초기 돌의 상태
    stones = list(map(int, input().split()))
    
    # 돌 뒤집기를 M번 진행한다.
    # i번째 돌을 사이에 두고 마주보는 j개의 돌에 대해 
    # 마주보는 돌이 같은색이면 뒤집고, 다른색이면 그대로 둔다
    # 주어진 돌을 벗어나는 경우 뒤집기는 중지된다.

    # 돌 뒤집기를 M번 진행해야하니 M번 반복
    for _ in range(M):
        # 뒤집기에 필요한 정보 i, j 입력받기
        i, j = map(int, input().split())

        # i는 1번부터 시작이므로 인덱스와 맞추기 위해 -1
        i -= 1

        # 마주보는 돌의 인덱스를 일단 계산해보면
        # i를 제외하고
        # (i-1, i+1) : 1개, (i-2, i+2) : 2개 ... (i-j, i+j) : j개
        # 마주보는 돌의 쌍은 총 j개
        # j번 반복하면서 마주보는 돌의 상태 조건에 따라 바꾸기
        # 조건 : 마주보는 돌(i-k,i+k) 가 같으면 바꾸기
        for k in range(1,j+1):
            # 왼쪽이나 오른쪽이 인덱스의 범위를 벗어나면 중단!
            if i-k < 0 or i+k >= N:
                break

            
            # 마주보는 두 돌의 색이 같다면
            if stones[i-k] == stones[i+k]:
                # 0이었으면 1로 바꾸고
                # 그게 아니면 0으로 바꾸고
                stones[i-k] = stones[i+k] = 1 if stones[i-k] == 0 else 0
        
    
    # 돌 뒤집기를 M번 하고 나서 돌의 상태 출력
    print(f"#{tc}", *stones)

