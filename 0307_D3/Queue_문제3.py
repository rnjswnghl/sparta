# GPT
from collections import deque  # deque는 큐(Queue)를 쉽게 사용할 수 있는 자료형입니다.

# 그래프 초기화 (인접 리스트 형태로)
graph = {
    1: [2, 3],  # 1번 노드는 2번, 3번과 연결됨
    2: [1, 4, 5],  # 2번 노드는 1번, 4번, 5번과 연결됨
    3: [1, 7],  # 3번 노드는 1번, 7번과 연결됨
    4: [2, 6],  # 4번 노드는 2번, 6번과 연결됨
    5: [2, 6],  # 5번 노드는 2번, 6번과 연결됨
    6: [4, 5, 7],  # 6번 노드는 4번, 5번, 7번과 연결됨
    7: [3, 6]  # 7번 노드는 3번, 6번과 연결됨
}

def bfs(start):
    visited = set()  # 방문한 노드를 기록하는 집합 (중복 방지용)
    queue = deque([start])  # 시작 노드를 큐에 넣음 (deque는 큐를 쉽게 다룰 수 있음)
    result = []  # 탐색한 노드들을 저장할 리스트 (결과값을 담을 곳)

    while queue:  # 큐에 노드가 남아 있을 때까지 반복
        node = queue.popleft()  # 큐에서 노드를 하나 꺼냄 (가장 먼저 들어온 노드를 꺼냄)
        
        if node not in visited:  # 꺼낸 노드가 아직 방문하지 않은 노드라면
            visited.add(node)  # 이 노드를 방문했다고 표시
            result.append(node)  # 결과 리스트에 이 노드를 추가
            
            # 현재 노드와 연결된 인접한 노드들에 대해 반복
            for neighbor in graph[node]:  # 현재 노드의 인접 노드들을 하나씩 확인
                if neighbor not in visited:  # 아직 방문하지 않은 인접 노드라면
                    queue.append(neighbor)  # 이 인접 노드를 큐에 넣음 (다음에 탐색할 노드로 추가)

    return result  # 모든 노드를 탐색하고 난 후, 탐색한 순서를 리스트로 반환

# BFS 실행 (1번 노드부터 탐색 시작)
bfs_result = bfs(1)

# 결과를 '-'로 구분하여 출력 (예: "1-2-3-4-5-7-6")
print("-".join(map(str, bfs_result)))
