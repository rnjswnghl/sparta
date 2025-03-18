# n이 주어졌을 때, 1부터 n까지의 합 구하기

n = int(input())

def sum_numbers(n):
    n_sum = 0
    for i in range(1, n+1):
        n_sum += i

    return n_sum

result = sum_numbers(n)

print(result)
