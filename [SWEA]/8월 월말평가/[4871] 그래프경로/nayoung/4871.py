# SWEA. 4871 그래프 경로

def dfs(S,visited):   # 미로 도착지점 발견하기 위한 dfs
    global res
    visited[S] = True # 방문 표시

    if S == G:  # 도착지점에 도달하면 재귀 종료 조건
        res = 1
        return

    for i in adjL[S]:  # 인접 노드 꺼내옴
        if not visited[i]:   # 방문하지 않은 정점
            dfs(i, visited)  # 재귀호출


T = int(input())  # 테스트 케이스 수 T

for case in range(1, T+1):
    V, E = map(int,input().split())  # V : 노드 / E : 간선 갯수
    graph = [list(map(int,input().split())) for _ in range(E)] #
    S, G = map(int,input().split())   # S : 출발 노드 / G : 도착 노드
    visited = [False]*(V+1)  # 방문 표시 확인 용
    res = 0
    # 인접리스트 생성
    adjL = [[] for _ in range(V+1)]
    for v1, v2 in graph:
        adjL[v1].append(v2)   # 방향 있는 그래프이기 때문에 각 부모 노드에 연결된 노드만 생성
    # print(adjL) [[], [4, 3], [3, 5], [], [6], [], []]
    dfs(S, visited)  # dfs 탐색 호출
    print(f'#{case} {res}')
