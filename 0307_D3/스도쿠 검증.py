# 스도쿠 숫자 퍼즐
# 가로 9칸, 세로 9칸. 1부터 9까지 입력
# 같은 줄에 한번씩 넣고, 
# 3x3 작은 격자에도 숫자 겹치기 않고 하나씩 입력
# 겹치는 숫자가 없을 경우, 1 출력. 아니면 0

# 첫 줄 테스트 케이스 개수 T
# 테스트 케이스
# 9x9 퍼즐 데이터

# 테스트 케이스 개수
T = int(input())
 
# 테스트 케이스 반복
for tc in range(1, T + 1):
    # 스도쿠 입력
    sudo = [list(map(int, input().split())) for _ in range(9)]
     
    # 행 검사 리스트
    r_count = [0] * 9
    # 열 검사 리스트
    c_count = [0] * 9
    # 스도쿠 유효성 검사 변수
    is_valid = True
 
    # 행과 열 검사
    for i in range(9):
        # 현재 행 초기화
        r_count = []
        # 현재 열 초기화
        c_count = []
 
        # 행과 열 검사
        for j in range(9):
            # i번째 행의 j번째 요소
            r_sudo = sudo[i][j]
            # j번째 행의 i번째 요소
            c_sudo = sudo[j][i]
 
            # 행에 추가 하기
            r_count.append(r_sudo)
            # 열에 추가 하기
            c_count.append(c_sudo)

        # 행 검사
        if set(r_count) != set(range(1, 10)):
            # 검사 실패면
            is_valid = False
            break
 
        # 열 검사
        if set(c_count) != set(range(1, 10)):
            # 검사 실패면
            is_valid = False
            break
 
    # 3×3 박스 검사
    if is_valid:
        # 3칸씩 이동
        for k in range(0, 9, 3):
            # 3칸씩 이동
            for m in range(0, 9, 3):
                # 박스 초기화
                box_nums = []
                 
                # 3개 안에서 순회
                for i in range(3):
                    # 3개 안에서 순회
                    for j in range(3):
                        # 검사할 박스에 넣기
                        box_nums.append(sudo[k + i][m + j])
 
                # 박스 안에 없으면 브레이크
                if set(box_nums) != set(range(1, 10)):
                    is_valid = False
                    break
 
    # 결과 출력
    print(f"#{tc} {1 if is_valid else 0}")