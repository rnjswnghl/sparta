# 학생들의 점수 학점 계산
# 학점은 상대평가, 총 10개의 평점
# A+, A0, A-, B+, B0, B-, C+, C0, C-, D0
# 학점은 중간/기말 점수 결과와 과제 점수 반영
# 총점 = 중간고사(35%) + 기말고사(45%) + 과제(20%)
# 총점이 높은 순대로 평점 부여
# 각각의 평점은 같은 비율로 부여 가능
# 각각의 학생들의 중간, 기말, 과제 점수 입력
# 학점을 알고 싶은 K번째 학생의 번호
# K번째 학생의 학점 출력

# 첫 줄은 총 테스트 케이스의 개수 T
# 다음 줄 학생수 N, 학점을 알고싶은 학생의 번호 K
# 다음 줄 각각의 학생이 받은 시험 및 과제 점수

# 테스트 케이스 개수
T = int(input())  

# 테스트 케이스 반복
for tc in range(1, T+1):
    # N : 학생 수, K : 학점을 알고 싶은 학생
    N, K = map(int, input().split())
    # 성적 저장할 변수
    scores = []  
 
    # 학생 수 만큼 반복
    for i in range(N):
        # mid : 중간, final : 기말, work : 과제
        mid, final, work = map(int, input().split())
        # 총점 계산
        total = mid * 0.35 + final * 0.45 + work * 0.2
        # scores에 총점과 학생 번호 저장. 1부터 번호 시작이라 +1
        scores.append((total, i + 1))
 
    # 총점 기준으로 내림차순 정렬
    scores.sort(reverse=True)
 
    # K번째 학생의 순위 찾기
    for rank in range(N):
        # scores는 (총점, 번호)순이므로 학생 순위 번호랑 찾는 번호가 같으면 
        if scores[rank][1] == K:
            # 반복 종료
            break
 
    grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    # 학점 구하기. 등수 // 같은 등급 받을 수 있는 수
    grade_idx = rank // (N // 10)
    print(f'#{tc} {grades[grade_idx]}')
