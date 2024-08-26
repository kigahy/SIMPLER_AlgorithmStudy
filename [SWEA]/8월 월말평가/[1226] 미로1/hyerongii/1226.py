import sys
from collections import deque
sys.stdin = open('input.txt')

# 1,1 부터 13,13 까지 갈 수 있는지 확인 BFS 사용하기
def bfs(arr, n):

    queue = deque()
    queue.append((1, 1))  # 출발점 표시
    visited = [[False]*n for _ in range(n)] # 방문한적 있는지 확인
    visited[1][1] = True # 출발지 방문 ok

    # 델타탐색
    dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    # 큐에 값이 있을 때 까지,, (끝까지 다 돈다면 queue에 값 없어짐)
    while queue:
        x, y = queue.popleft()
        # 탈출조건 13, 13 인 도착지에 도착한다면 1 반환
        if x == 13 and y == 13:
            return 1
        # 델타로 돌리면서
        for dx, dy in dxy:
            nx, ny = x+dx, y+dy
            # 범위 벗어나면
            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
            # 값이 1이면(벽이면)
            if arr[nx][ny] == 1: continue
            # 방문한적 있으면
            if visited[nx][ny]: continue
            # 제외처리하고 이동
            queue.append((nx, ny))
            # 방문한 곳 표시
            visited[nx][ny] = True
    # 목적지 도착하지 않고 다 돌아버리면 0 반환
    return 0

for _ in range(10):
    tc = input()
    N = 16
    arr = [list(map(int, list(input()))) for _ in range(N)]
    # 결과 0, 1 로 리턴하기
    result = bfs(arr, N)
    print(f'#{tc} {result}')

