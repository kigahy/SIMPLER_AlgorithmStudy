import sys
sys.stdin = open("input.txt", "r")

# 델타 사용, 플러스, 엑스 모양일때 각각 값 구해주고 그중에서 큰 값 구하기
# + 모양일 때: 위, 오른쪽, 아래, 왼쪽
dxy_p = [[-1, 0], [0, 1], [1, 0], [0, -1]]
# x 모양일 때: 왼쪽위 오른쪽위 오른쪽아래 왼쪽아래
dxy_x = [[-1, -1], [-1, 1], [1, 1], [1, -1]]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = arr[0][0]
    for i in range(N):
        for j in range(N):
            # 가운데 값 미리 더해주기
            sum_p = arr[i][j]
            sum_x = arr[i][j]
            for k in range(1, M):
                # 플러스모양일때
                for dx, dy in dxy_p:
                    nx = dx*k+i
                    ny = dy*k+j
                    if 0 <= nx < N and 0 <= ny < N:
                        sum_p += arr[nx][ny]
                # 엑스모양일때
                for dx, dy in dxy_x:
                    nx = dx*k+i
                    ny = dy*k+j
                    if 0 <= nx < N and 0 <= ny < N:
                        sum_x += arr[nx][ny]
            # 큰 값 구해주기
            ins_max = max(sum_p, sum_x)
            if max_v < ins_max:
                max_v = ins_max
    print(f'#{tc} {max_v}')
