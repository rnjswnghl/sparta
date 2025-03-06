T = int(input())

for tc in range(1, T+1):
    # N : A의 길이
    # M : B의 길이
    N, M = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 문제에서 원하는 답은 곱해서 더했을때 최대값
    MAX_VALUE = -999999

    # 둘 중에 작은쪽을 한칸씩 밀면서 곱해보기

    # 한칸씩 미는 작업을 총 몇번 하게 될까?
    # 긴 리스트의 길이 - 작은 리스트의 길이 만큼
    for i in range(max(M,N) - min(M,N) + 1):
        # i는 몇칸 밀었는지를 의미함과 동시에
        # i는 밀고 나서 긴 리스트의 원소를 곱하기 시작하는 인덱스를 의미함
        
        # i번 밀었을때 각 원소를 곱해서 더한 값
        v = 0
        
        # 작은 리스트의 원소는 항상 0번 인덱스부터 곱하기 시작
        for j in range(min(M,N)):
            # A가 B보다 길면
            if N > M:
                v += A[i+j] * B[j]
            # B가 A보다 길거나 같으면
            else:
                v += B[i+j] * A[j]

        # 방금 곱해서 더한 값과 이전에 구한 값 중 최대값 구하기
        MAX_VALUE = max(MAX_VALUE, v)
    
    print(f"#{tc} {MAX_VALUE}")

