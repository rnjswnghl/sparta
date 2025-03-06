T = int(input())

for tc in range(1, T + 1):
    # N : 학생의 수
    # K : 학점을 알고싶은 학생의 번호
    N, K = map(int, input().split())

    # 학생들의 점수 리스트
    students = []

    # 학생의 번호 i는 1번부터 시작, 모든 학생의 점수 반복해서 입력받기
    for i in range(1, N + 1):
        # i번 학생의 중간, 기말, 과제 점수
        mid, final, work = map(int, input().split())

        # 총점이 같은 경우는 없다!
        # 비율이라고 해서 굳이 100으로 나눌 필요는 없음
        # 가중치만 곱해서 부여
        score = mid * 35 + final * 45 + work * 20

        # 학생 점수 리스트에 점수와 학생번호를 튜플로 묶어서 추가
        # (i번 학생의 점수, 학생번호i)
        students.append((score, i))

    # students 리스트를 정렬하면 튜플의 맨 앞 원소(학생의 점수) 기준으로 내림차순 정렬
    students.sort(reverse=True)

    # 성적은 A+ 부터 D0 까지 총 10개의 등급
    grade_table = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
    # 인덱스를 각 성적의 번호로 생각
    # A+ : 0 / A0 : 1 / A- : 2 .... D0 : 9

    # 등급 하나당 받을 수 있는 학생의 수는??
    # 평점은 같은 비율로 부여한다고 했으므로
    # 학생 수가 N 명이면 등급이 10개이므로
    # 등급 하나당 받을수 있는 학생 수를 M 이라고 하면
    # M = N//10
    M = N // 10

    # students 리스트는 내림차순 정렬 되어있으므로
    # 0번 인덱스부터 M-1 까지 학생은 A+
    # M번 인덱스부터 2*M-1 까지 학생은 A0
    # ...
    # 이런식으로 찾다가 K번 학생을 찾으면 종료

    # 모든 학생을 확인하며
    # 등급을 하나씩 부여하는데
    # 지금까지 내가 같은 등급을 몇명에 부여했는지 셀 카운트 변수와
    # 몇번 등급을 부여하고 있는지 알 수 있는 등급 인덱스 변수 필요
    
    # 등급 인덱스, 성적은 내림차순 정렬 되어있으므로 최상위 성적인 A+ 부터 시작
    # A+ 는 0번
    grade_idx = 0

    # 등급을 부여한 학생 수, M번 부여했다면 등급 인덱스 1 증가시키고, 다시 0명부터 시작
    cnt = 0

    for score, i in students:
        # i가 학생번호인데, 우리가 찾는 K번 학생이면 찾음
        if i == K:
            # 현재 i번 학생에 부여할 등급을 출력하고 종료
            print(f"#{tc} {grade_table[grade_idx]}")
            break
        
        # 등급 부여하기
        cnt += 1
        # 등급당 제한 인원 체크, M명 부여했으므로 다음 등급 부여 시작
        if cnt == M:
            cnt = 0
            grade_idx += 1


