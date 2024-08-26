import sys
sys.stdin = open("input.txt", "r")
from collections import deque

# 최소 간선 개수여서 BFS로 풀자!
# 그래프 문제는 인접행렬(인접리스트)로 풀기
def bfs(S, G):
    queue = deque()
    # 출발노드 표시 (현재위치랑 간선개수 같이 묶어서 보기)
    queue.append((S, 0))
    # 방문한적 있는지 확인, 여기에 최소 거리도 같이 넣어주기
    visited = [0] * (V + 1)
    # 시작점 방문표시
    visited[S] = 1

    while queue:
        current, num = queue.popleft()
        for i in range(1, V+1):
            # 시작점에서 인접한 정점 중 방문하지 않은 정점
            if adjL[current][i] and not visited[i]:
                # 목적지 도착했다면
                if i == G:
                    # 최소거리 반환(여기서 +1 안해주니까 답 달랏음)
                    return num+1
                # 큐에 추가 하고 최소거리 늘려주기
                queue.append((i, num+1))
                # 방문 확인
                visited[i]=1
    # 만약 연결 안되어있으면
    return 0

T = int(input())
for tc in range(1, T+1):
    # V = 노드개수 E = 간선개수
    V, E = map(int, input().split())
    # 인접리스트 만들기
    adjL = [[0]*(V+1) for _ in range(V+1)]
    # 양쪽 노드 번호 받아서 인접한지 체크 후 표시, 그래프 방향 x
    for _ in range(E):
        v1, v2 = map(int, input().split())
        adjL[v1][v2] = 1
        adjL[v2][v1] = 1
    # S = 출발노드 G = 도착노드
    S, G = map(int, input().split())
    result = bfs(S,G)
    print(f'#{tc} {result}')


