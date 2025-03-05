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

T = int(input())

for tc in range(1, T+1):
    N, K = map(int,input().split())
    score = []

    for _ in range(N):
        mid, final, work = map(int, input().split())
        total_score = mid * 0.35 + final * 0.45 + work * 0.2
        score.append(total_score)

    sort_score = sorted(score)
    target = score[K-1]

    rank = sort_score.index(target)

    grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    grade_idx = (rank * 10) // N 
    result = grades[grade_idx]      


    print(f'#{tc} {result}')