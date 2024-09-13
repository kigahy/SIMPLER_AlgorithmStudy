# 노드들 중에서 방문한거 체크하면서 연결되어있으면 쭉쭉 가고 한번 돌 때 카운트 1
# 방문안했으면 다음 노드 체크
# dfs로 풀기

def dfs(node, arr, visited):
    visited[node] = True                # 방문한 곳 표시

    for j in range(len(arr)):           # 노드의 노드 쭉 돌기
        if arr[node][j] and not visited[j]: # 연결되어 있고 방문한적 없다면 탐색
            dfs(j, arr, visited)        # 그 노드로 가기

def solution(n, arr):
    visited = [False] * n               # 방문 확인 용 리스트 만들기
    cnt = 0                             # 네트워크 개수 세는 변수

    for i in range(n):                  # 노드 순차적으로 dfs 탐색
        if not visited[i]:              # 방문한적 없는 노드라면
            cnt += 1                    # 카운트 증가
            dfs(i, arr, visited)        # 탐색

    answer = cnt
    return answer

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

print(solution(3, computers))
