# 그래프 경로 dfs 사용해주기
# 도착한적 있는지 없는지 확인해주기 위해서 

def dfs(current, adjL, visited):
    # 현재 좌표 방문한적 있으면 True 체크하고 넘어가기
    visited[current] = True
    # 그리고 현재 좌표 리스트에 추가 - 도착하는지 알아보기 위해 ㅠㅠ
    current_lst.append(current)
    # 열마다 탐색하면서
    for i in range(len(adjL)):
        # 연결되어있고, 방문한적 없으면 또 반복해주기
        if adjL[current][i] and not visited[i]:
            dfs(i, adjL, visited)

T = int(input())
for tc in range(1, T + 1):
    # V = 노드개수 E = 간선 개수
    V, E = map(int, input().split())
    # 인접행렬 만들어주려고 우선 노드만큼 0 행렬 만듬
    adjL = [[0] * (V + 1) for _ in range(V + 1)]
    # 간선 정보 얻으면서 인접행렬 체크해주기
    # 이때 화살표 방향 있기 때문에, V1 -> V2 만 1
    # 화살표 방향 없다면 adjL[v2][v1]=1 추가
    for _ in range(E):
        v1, v2 = map(int, input().split())
        adjL[v1][v2] = 1  # 화살표 있음
    # S = 출발 노드 G = 도착노드
    S, G = map(int, input().split())

    # 방문한적 있는지 확인용으로 만들기 이때 인접행렬이랑 행 수 동일하게
    visited = [False] * (V + 1)
    current_lst = []
    # dfs 돌리기
    dfs(S, adjL, visited)
    # 만약 도착지점이 현재 좌표에 있으면
    if G in current_lst:
        result = 1
    # 없다면
    else:
        result = 0

    print(f'#{tc} {result}')