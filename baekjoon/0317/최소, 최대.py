# N개의 정수가 주어진다. 최솟값과 최댓값을 구하는 프로그램 작성

# 입력
# 첫째 줄에 정수의 개수 N
# 둘째 줄에는 N개의 정수를 공백으로 구분
# 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.

N = int(input())
numbers = list(map(int, input().split()))

max_numbers = max(numbers)
min_numbers = min(numbers)

print(f'{min_numbers} {max_numbers}')
