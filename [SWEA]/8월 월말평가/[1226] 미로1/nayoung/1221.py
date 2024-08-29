# 4875 [미로1]

def dfs(miro, x,y):  # 도착지점 3을 찾기 위한 dfs탐색 함수
    global res  # 전역변수 res 값 변경위함
    dxy = [[0,1], [1,0], [0,-1], [-1,0]]  # 우, 하, 좌, 상

    visited[x][y] = 1  # 방문 표시
    for dx,dy in dxy:  # 델타 탐색
        nx, ny = x+dx, y+dy
        if miro[nx][ny] == 3:   # 3(도착지점) 찾으면 res = 1로 할당하고 함수 리턴
            res = 1
            return
        if 0<=nx<box_size and 0<=ny<box_size and miro[nx][ny] == 0 and visited[nx][ny] == 0:
            # 인덱스 범위 안과 방문하지 않고 미로가 0(통로)인 곳만 탐색
            dfs(miro, nx,ny)   # 재귀 호출
    return res

box_size = 16

for _ in range(1,11):
    case = int(input())  # 테케 입력
    miro = [list(map(int,input())) for _ in range(box_size)]
    visited = [[0]*box_size for _ in range(box_size)]  # 방문했는지 확인하기 위함
    res = 0   # 도착지점 찾았는지 확인하기 위한 정답 변수 설정

    for i in range(box_size):
        for j in range(box_size):
            if miro[i][j] == 2:  # 요소 돌다가 출발지점(2)인 곳 찾으면 해당 좌표를 가져오고 탐색 종료
                x, y = i, j
                break
    print(f'#{case} {dfs(miro, x, y)}')