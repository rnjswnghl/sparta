def dfs(swap_cnt):
    global max_result
    if swap_cnt == total_swap_cnt:
        max_result = max(max_result, int(''.join(number)))
        return
  
    for i in range(len(number)):
        for j in range(i + 1, len(number)):
            number[i], number[j] = number[j], number[i]

            str_number = ''.join(number)
            if visited.get((swap_cnt, str_number)) is None:
                visited[(swap_cnt, str_number)] = 1
                dfs(swap_cnt + 1)
                
            number[i], number[j] = number[j], number[i]


T = int(input())

for tc in range(1, T + 1):

    number, total_swap_cnt = input().split()
    number = list(number)
    total_swap_cnt = int(total_swap_cnt)
    max_result = -1   
    
    visited = {}
    
    dfs(0)
    print(f'#{tc} {max_result}')