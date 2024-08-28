# 강사님께 여쭤보고 받은 코드이며, BFS 방식입니다.

import sys
sys.stdin = open('input.txt')


def BFS(n, count): # 출발노드와 카운트
    q = [(n, count)]
    visited[n] = 1 # 출발노드 방문함
    while q:
        target = q.pop(0) # 출발지점 끄집어냄
        n = target[0] # 출발지점을 새 변수에 할당
        count = target[1] # 몇번 갔는지 count에 저장. q의 count가 됨
        # n, count = q.pop(0)
        for w in range(1, V+1):  # 정점 수만큼 반복
            if mat[n][w] and not visited[w]:
                if w == G:
                    return count + 1
                visited[w] = 1
                q.append((w, count + 1))


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split()) # 노드 수, 간선 수
    arr = [list(map(int, input().split())) for _ in range(E)] # 간선의 시작과 끝
    S, G = map(int, input().split()) # 출발노드, 도착노드
    mat = [[0] * (V+1) for _ in range(V+2)] # 인접 행렬
    visited = [0] * (V+2) # 방문했는지
    for info in arr: # 인접행렬에 값 넣음
        mat[info[0]][info[1]] = 1
        mat[info[1]][info[0]] = 1
    count = BFS(S, 0) # 출발노드와 0 보냄
    print(f'#{tc} {count}')
