# 음료수 얼려 먹기

'''
N X M 크기의 얼음 특이 있습니다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시됩니다.

구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서루 연결되어 있는 것으로 간주합니다.

이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하세요.

다음의 4X5 얼음 틀 예시에서는 아이스크림이 총 3개 생성됩니다.

[입력조건]

- 첫번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어집니다. (1<=N, M<=1,000)

- 두번째 줄부터 N+1번째 줄까지 얼음 틀의 형태가 주어집니다.

- 이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1입니다.

[출력조건]

- 한 번에 만들 수 있는 아이스크림의 개수를 출력합니다.


'''
import sys
sys.stdin = open('input.txt', 'r')


def dfs(x, y):

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if visited[nx][ny] == 0 and arr[nx][ny] == '0':
            visited[nx][ny] = 1  # 방문 표시
            dfs(nx, ny)

T = int(input())

for case in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(input()) for _ in range(N)]
    visited = [[0] * (M) for _ in range(N)]

    dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    ans = 0

    for i in range(N):
        for j in range(M):

            if arr[i][j] == '0':
                if visited[i][j]==1:
                    continue
                visited[i][j] = 1
                dfs(i,j)
                ans+=1
    print(f'#{case} {ans}')
