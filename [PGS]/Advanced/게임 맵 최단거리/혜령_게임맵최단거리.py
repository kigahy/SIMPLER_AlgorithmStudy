from collections import deque
def solution(maps):
    # 캐릭터는 항상 1,1 위치에 있음
    # 상대방은 항상 n,m 위치에 있음 point!!

    # maps로 n, m 알아내기
    n = len(maps)
    m = len(maps[0])

    # bfs로 델타 돌려서 최소 거리 찾기
    dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    start = [0, 0]
    visited = [[-1]*m for _ in range(n)]

    q = deque()
    q.append(start)
    # visited 에 시작점 부터 값 증가시켜주기
    visited[0][0] += 1

    while q:
        x, y = q.popleft()

        # 상대방 좌표에 도착하면 끝!
        if x == m-1 and y == n-1:
            break

        for dx, dy in dxy:
            nx, ny = x+dx, y+dy
            if 0 > nx or nx >= n or 0 > ny or ny >= m or visited[nx][ny] > -1 or maps[nx][ny] == 0: continue
            # 다른 칸으로 이동할때마다 visited에 거리 증가시켜서 값 넣어주기
            visited[nx][ny] = visited[x][y] + 1   
            q.append([nx, ny])

    # 최소거리는 visited의 목적지 좌표 값임!
    answer = visited[n-1][m-1]

    # 도착지 거리도 포함해야해서 +1 해주기
    if answer > -1:
        answer += 1

    return answer

