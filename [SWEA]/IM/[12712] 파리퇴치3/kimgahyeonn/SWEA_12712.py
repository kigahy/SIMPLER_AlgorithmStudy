T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    cross_dxy = [[0,1],[1,0],[0,-1],[-1,0]] # + 모양 행, 열
    dia_dxy = [[1,1],[1,-1],[-1, -1],[-1,1]] # x 모양

    result = 0 # 최댓값 담을 변수 선언

    for x in range(N) : # 가로만큼
        for y in range(N) : # 세로만큼

            cross = lst[x][y]
            dia = lst[x][y]
            for cx, cy in cross_dxy : # + 모양의 4방향 각각 순회
                for c in range(1, M) : # 현재 위치 시점으로 분사만큼
                    cross_x = x + cx * c # k마다 늘어나는 행
                    cross_y = y + cy * c # k마다 늘어나는 열

                    if 0 <= cross_x < N and 0 <= cross_y < N : # 인덱스를 벗어나지 않는지 검사
                        cross += lst[cross_x][cross_y] # + 분사 합계 변수에 저장

            for dx, dy in dia_dxy : # x 모양의 4방향 순회
                for d in range(1, M) : # 현재 위치 시점으로 분사만큼
                    dia_x = x + dx * d # 한 대각선만큼 범위 늘어남
                    dia_y = y + dy * d # 다른 대각선만큼 범위 늘어남

                    if 0 <= dia_x < N and 0 <= dia_y < N : # 인덱스를 벗어나지 않는지 검사
                        dia += lst[dia_x][dia_y] # x 분사 합계 변수에 저장

            if cross > result: # cross와 dia 중 큰 값을 검사
                result = cross
            if dia > result:
                result = dia
        
    print(f'#{tc} {result}')


                    

