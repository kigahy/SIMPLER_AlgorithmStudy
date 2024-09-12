import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs(i):
    # 출발점 표시
    q = deque()
    q.append(i)

    # 출발점 방문 표시
    visited[i] = 1

    # 도착점 있을 때 까지 반복
    while q:
        # 현재위치 반환
        x = q.popleft()

        # 현재 노드에서 인접한 노드 다 돌리기
        for j in adj[x]:
            if not visited[j]:      # 방문 안했으면
                q.append(j)         # 인큐
                # 이 형태 BFS에서 많이 쓰인다고 함 - 최소 거리수 같은거 구할 때
                visited[j] = visited[x] + 1   # 방문했다고 표시하고, 마지막까지 거쳐간 수 더해주기

# 인풋 받기
for tc in range(1, 11):
    # N: 입력받는 데이터의 길이, start: 시작점
    N, start = map(int, input().split())
    arr = list(map(int, input().split()))

    # 인접리스트 만들기 <- 간선 내용 이중 리스트로 넣어줄거임
    # 사람 최대 100명 (0번 안쓸거임)
    adj = [[] for _ in range(101)]

    for i in range(N//2):
        x = arr[2*i]        # 출발지
        y = arr[2*i+1]      # 목적지
        adj[x].append(y)    # 화살표 방향 있어서 x->y 로 값 넣어주기

    # 방문리스트 만들기
    visited = [0] * 101

    # bfs 돌려주기
    bfs(start)

    # visted 에서 마지막 방문한 게 거리수 제일 큰거임
    max_v = max(visited)

    # 제일 큰 거리수의 인덱스 찾고 그중에서 값 제일 노드가 답임
    last_num = 0
    for i in range(101):
        if max_v == visited[i]:
            if last_num < i:
                last_num = i

    print(f'#{tc} {last_num}')
