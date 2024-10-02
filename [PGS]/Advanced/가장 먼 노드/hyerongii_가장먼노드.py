'''
n개의 노드가 있는 그래프가 있습니다.
각 노드는 1부터 n까지 번호가 적혀있습니다.
1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 합니다.
가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미합니다.

노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때,
1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 하도록 solution 함수를 작성해주세요.
'''
from collections import deque

def bfs(node, n, graph):
    # visited 생성, 거리 값 갱신할거임
    visited = [0] * (n + 1)

    # bfs 사용
    q = deque()
    visited[node] += 1
    q.append(node)

    while q:
        current = q.popleft()
        for nd in graph[current]:
            if not visited[nd]:
                q.append(nd)
                # 방문한 곳 거리 +1씩 계속 해주기
                visited[nd] = visited[current]+1
    return visited

def solution(n, edge):
    # 그래프 인접 리스트 생성, index -> 출발 노드로 생각해줌
    graph = [[] for _ in range(n+1)]

    for v in edge:
        # 간선 양방향이어서 인접 정보 양방향 추가
        graph[v[0]].append(v[1])
        graph[v[1]].append(v[0])

    # 구하려고 하는 것은 1번 노드 부터 가장 멀리 떨어진 노드의 갯수
    # visited로 거리 계산해서 최대인 노드 몇 개인지 세기 -> bfs 사용
    visited = bfs(1, n, graph)

    # visited에서 가장 값 큰거 개수 세주기
    max_v = max(visited)
    answer = 0

    for dist in visited:
        if max_v == dist:
            answer += 1

    return answer

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

print(solution(n, edge))
