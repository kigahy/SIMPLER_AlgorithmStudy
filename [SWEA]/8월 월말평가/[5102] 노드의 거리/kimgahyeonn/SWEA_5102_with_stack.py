# 강사님께 여쭤보고 받은 코드이며, DFS 방식입니다.
# 제 코드에서 def dfs부분을 수정한 코드입니다.

import sys
sys.stdin = open('input.txt')

T = int(input())  # 테스트케이스 10개중에 5개만 맞음


def dfs(s, G):
    stack = [(s, 0)]  # 다음 조사 대상
    visited = [9999] * (V + 1)  # 충분 히 큰 수
    visited[s] = 0  # 첫 조사 시작 지점은 count 0

    while stack:    # 조사 대상이 있는 동안
        v, count = stack.pop()  # 조사 대상 노드 번호와 지금까지 소요한 시간
        for w in data[v]:  # 부모노드의 자식노드를 순회
            print(visited, w)
            if visited[w] >= count + 1:  # 이전번 누군가 방문한 정보가 지금보다 더 오래 걸렸다면
                visited[w] = count + 1  # 다음 위치 까지의 값 갱신
                stack.append((w, count+1))  # 다음 조사 대상 추가
        if v == G:  # 시작점부터 끝 노드까지 다 돌면
            return count
    return 0  # 시작점과 끝점이 연결되지 않았다면 0 리턴


for tc in range(1, T + 1):
    V, E = map(int, input().split())  # 정점 수, 간선 수
    arr = [list(map(int, input().split())) for _ in range(E)]  # 간선 양쪽의 노드 번호
    S, G = map(int, input().split())  # 출발 노드, 도착 노드

    data = [[] for _ in range(V + 1)]  # 해당 인덱스 번호에 해당하는 노드의 인접 노드가 몇개인지 모르니 []로 선언

    for i in range(E):  # 각 하나의 간선에 대하여
        v1 = arr[i][0]  # 시작 정점의 값
        v2 = arr[i][1]  # 끝나는 정점의 값

        data[v1].append(v2)  # 인덱스 번호로 인접 노드 찾기 위하여 저장
        data[v2].append(v1)
    result = dfs(S, G)
    print(f'#{tc} {result}')

