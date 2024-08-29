# 원래 res 변수를 안 쓰고 return 1, return 0으로 바로 숫자로 리턴했다.
# 그런데 그러니까 결과값이 모두 0으로 출력되었다...
# 나영언니 코드 보고 res 변수를 추가해 보았는데 이게 된다! 난 똑같다고 생각하는데 왜 결과가 다르지?
# 아무튼 이번 코드는 낯설었던 visited를 잘 활용하여 방문체크를 해보았다.
# BFS 정석대로 큐 이용해서 푸는 방법도 알고 싶다. 아직 그 레벨은 안되는 것 같아서(..) 이렇게 했는데 한번쯤 시도해 보고 싶음.

import sys
sys.stdin = open("input_1226.txt", "r")

def Maze(row, column, N) :
    global res
    dxy = [[0,1], [1,0], [0,-1], [-1,0]] # 델타탐색
    visited[row][column] = 1

    for dx, dy in dxy :
        nx = row + dx
        ny = column + dy

        if wall[nx][ny] == 3 : # 도착지점 찾기
            res = 1

        if wall[nx][ny] != 1 and visited[nx][ny] != 1 and 0 <= nx < N and 0 <= ny < N : # 벽이 아니고 방문하지 않았고 인덱스를 벗어나지 않았다면 재귀호출
            Maze(nx, ny, N)

    return res

for tc in range(10) :
    tc_num = int(input())
    N = 16 # 가로세로 길이
    wall = [list(map(int, input().strip())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    res = 0

    start_row = 0 # 시작지점 행
    start_column = 0 # 시작지점 열
    for i in range(N) : # 시작지점 행 열 찾는 반복문
        for j in range(N) :
            if wall[i][j] == 2 : # 2라면 그게 시작점
                start_row = i
                start_column = j

    result = Maze(start_row, start_column, N) # 시작 인덱스와 배열의 가로세로 길이를 인자로 넘김
    print(result)