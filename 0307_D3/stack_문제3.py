# GPT
# 간선 정보 (순서대로 입력)
edges = [(1, 2), (1, 3), (2, 4), (2, 5), (4, 6), (5, 6), (6, 7), (3, 7)]

# 그래프를 인접 리스트 형식으로 구성
graph = {}

# 주어진 간선 정보를 바탕으로 그래프를 구성합니다.
for u, v in edges:
    if u not in graph:
        graph[u] = []  # u가 그래프에 없으면 빈 리스트로 초기화
    if v not in graph:
        graph[v] = []  # v가 그래프에 없으면 빈 리스트로 초기화
    graph[u].append(v)  # u의 이웃에 v를 추가
    graph[v].append(u)  # v의 이웃에 u를 추가 (무방향 그래프)

# 스택을 사용한 DFS 함수
def dfs(graph, start):
    # 방문한 정점을 기록할 집합
    visited = set()

    # 스택에 시작 정점을 넣고 탐색을 시작합니다.
    stack = [start]

    # 스택이 빌 때까지 반복 (스택이 비면 더 이상 탐색할 정점이 없다는 의미)
    while stack:
        # 스택에서 정점을 하나 꺼냅니다.
        node = stack.pop()

        # 이미 방문한 정점이면 지나갑니다.
        if node in visited:
            continue

        # 정점을 방문했으므로 출력하고, 방문한 정점으로 기록합니다.
        print(node, end='-')
        visited.add(node)

        # 현재 정점의 이웃들을 스택에 넣습니다.
        # 이웃은 오름차순으로 넣어야 작은 번호의 정점부터 먼저 탐색됩니다.
        for neighbor in sorted(graph[node], reverse=True):  # 역순으로 넣어서 나중에 작은 번호가 먼저 나옵니다.
            if neighbor not in visited:
                stack.append(neighbor)

# DFS 시작 (시작 정점: 1)
dfs(graph, 1)
