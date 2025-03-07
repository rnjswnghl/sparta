# i번째 돌을 사이에 두고 마주보는 j개의 돌에 대해
# 각각 같은 색이면 뒤집고, 다른 색이면 그대로 둔다.
# 주어진 돌을 벗어나는 경우 뒤집기 중지

# 게임의 개수 T
# 돌의 수 N, 뒤집기 횟수 M
# 돌의 초기 상태 origin
# 기준 돌 i, 마주보는 돌 개수 j

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    origin = list(map(int, input().split()))

    for _ in range(M):
        i, j = map(int, input().split())
        c = j // 2

        for k in range(N):
            if origin[k] == i-1:
                for m in range(i-c, i+c-1):
                    origin[k-c]