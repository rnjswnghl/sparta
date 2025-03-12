T = int(input())

for tc in range(1, T+1):
    # N : 돌 개수
    # M : 돌 뒤집는 횟수
    N, M = map(int, input().split())

    # 돌의 초기 상태
    stones = list(map(int, input().split()))

    # 뒤집기는 i번째 돌부터 j개의 돌을 i번째 돌과 같은 색으로 바꾼다
    # i, j 가 M 번 입력되니 반복문 M번짜리 필요
    for _ in range(M):
        # i : 바꾸기 시작하는 돌 번호
        # j : 바꾸는 개수
        i, j = map(int, input().split())

        # 돌 번호가 1부터 시작하므로 인덱스로 바꾸려면 -1 해주기
        i -= 1

        # stone 배열의 i번 인덱스부터 j개의 돌을 i번 돌의 색과 같은 색으로 바꾸기
        # 바꿔야 하는 돌의 인덱스 범위는 range(i, i+j)
        for s in range(i, i+j):
            # 바꾸는 돌의 인덱스 s가 배열의 범위인 N을 넘어가지 않도록 주의!
            if s < N:
                stones[s] = stones[i]

    # 뒤집기를 M번 한 이후 돌의 상태 출력
    print(f"#{tc}" , *stones)
