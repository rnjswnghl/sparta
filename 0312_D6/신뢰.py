# 두 로봇을 서로 다른 복도에 가둬놓고, 실험을 진행
# 한 복도에는 1 이상 100 이하의 정수로 구분되는 100개의 버튼 존재
# 버튼 K는 복도의 시작점에서 K미터 떨어져 있다. 두 로봇은 버튼 1에서 시작
# 매 1초마다, 로봇은 복도의 양 방향 중 하나로 1미터 걷거나, 
# 자기 위치에 있는 버튼을 누르거나, 아무 것도 하지 않는다.
# 오렌지와 블루는 서로 다른 복도에 있음에 유의
# 하나의 테스트는 여러 개의 버튼 수열로 표시되는데, 
# 이는 수열에 표시된 순서대로 버튼을 눌러야 함
# 순서대로 버튼을 눌러야 하기 때문에, 두 로봇이 동시에 버튼을 누를 수는 없다. 
# 두 로봇 모두 수열을 정확히 알고 있다.
# 테스트를 끝낼 수 있는 가장 빠른 시간은 언제인가?

# 첫 줄에 테스트 케이스의 수 TC가 주어진다. 
# 다음 줄 TC개의 테스트 케이스가 새 줄로 구분되어 주어진다.
# 1. 첫 번째 정수는 테스트에서 눌러야 하는 버튼의 개수 N 이다. (1 <= N <= 100)
# 2. 이후 버튼 N개가 공백으로 구분되어 한 줄에 주어진다.
# 버튼이 “O x” 의 형태이면 오렌지가 버튼 x를 눌러야 하며,
# “B x”의 형태이면 블루가 버튼 x를 눌러야 한다. (1 <= x <= 100)

def min_time(commands):
    # 오렌지와 블루의 시작 위치
    orange_pos, blue_pos = 1, 1
    # 오렌지와 블루의 현재 소요 시간
    orange_time, blue_time = 0, 0
    # 전체 소요 시간
    total_time = 0

    for robot, target in commands:
        # 목표 버튼 위치 정수 변환
        target = int(target)

        if robot == 'O':
            # 이동 시간
            move_time = abs(target - orange_pos)
            # 목표 위치 이동  
            orange_pos = target
            # 버튼 누르기 포함
            orange_time = max(orange_time + move_time, total_time) + 1
            # 전체 시간 업데이트
            total_time = orange_time
        else:  # 'B'인 경우
            # 이동 시간
            move_time = abs(target - blue_pos)
            # 목표 위치 이동
            blue_pos = target
            # 버튼 누르기 포함
            blue_time = max(blue_time + move_time, total_time) + 1
            # 전체 시간 업데이트
            total_time = blue_time

    return total_time


# 테스트 케이스 개수 입력
T = int(input())
# 테스트 케이스 반복
for t in range(1, T + 1):
    # N과 지시 사항 입력 받기
    data = input().split()
    # data 첫 요소는 명령 횟수 N  
    N = int(data[0])
    # 명령은 1에서 지시횟수의 2배까지의 범위.(0번은 N)
    # 블루와 오렌지 각각 명령을 번갈아서 받으니 2씩 간격으로 설정
    # i번 요소와 i+1번 요소는 세트!
    # 범위 안에서 i는 B 또는 O를 가리키며, i+1은 버튼의 위치를 나타냄

    commands = [(data[i], data[i + 1]) for i in range(1, 2 * N, 2)]
    result = min_time(commands)
    print(f"#{t} {result}")
