T = int(input())

for tc in range(1, T + 1):
    N = 9
    sudoku = [list(map(int, input().split())) for _ in range(N)]

    # 일단 잘 되어 있다고 생각
    answer = 1

    # 스도쿠가 잘 되어있는지 판단하려면
    # 1. 가로, 세로에 1~9 9개의 숫자가 중복없이 존재
    # 2. 3 * 3 크기의 정사각형에 1~9 9개의 숫자가 중복없이 존재

    # 1번 조건을 검사하기 위해 생각한 풀이
    # 행우선순회 / 열우선순회 하면서 숫자 set 에 모두 넣어버리면
    # 중복이 존재하지 않으면 set의 크기는 9
    # 중복이 존재하면 set의 크기는 < 9
    for i in range(N):
        # 가로 숫자 세기
        row_set = set()
        # 세로 숫자 세기
        col_set = set()
        for j in range(N):
            row_set.add(sudoku[i][j])
            col_set.add(sudoku[j][i])

        # 행검사, 열검사
        if len(row_set) != N or len(col_set) != N:
            answer = 0

    # 2번 조건을 검사하기 위해 생각한 풀이
    # 9*9 스도쿠를 9등분해서 3*3 스도쿠 9번 검사
    # 위와 마찬가지로 3*3 크기 정사각형 순회하면서 숫자 set에 추가
    # set의 크기 == 9 : 스도쿠 정상
    # set의 크기 < 9 : 스도쿠 비정상 (중복 숫자 존재)

    # (i,j) : 작은 3*3 정사각형의 왼쪽 위 시작 위치 
    # (0,0), (0,3), (0,6)
    # (3,0), (3,3), (3,6)
    # (6,0), (6,3), (6,6)
    for i in range(0, N, 3):
        for j in range(0, N, 3):
            box_set = set()
            # (r,c) : 작은 정사각형 내에서 순회하는 위치
            for r in range(i, i + 3):
                for c in range(j, j + 3):
                    box_set.add(sudoku[r][c])

            # print(i,j, box_set)
            if len(box_set) != N:
                answer = 0

    print(f"#{tc} {answer}")