# 못풀었습니다...

T = int(input())


for tc in range(1, T + 1):
    N, M = map(int, input().split()) # 가로길이, 세로길이. 열, 행
    lst = [list(map(int, input().split()))for _ in range(M)]

    # 델타 탐색 1의 기준은 오른쪽, 아래쪽, 왼쪽, 위쪽 순서대로 감
    # 가로길이, 세로길이를 탐색하기 위함. 왼쪽에서 오른쪽으로 쭉 이동하는 0,1 그리고 위에서 아래로 쭉 떨어지는 1,0만을 취급함
    dxy = [[0,1], [1,0]]

    result = 0

    for i in range(M) : # 행만큼 반복하는데 세로길이를 입력받은 M이 곧 행이 됨
        for j in range(N) : # 열만큼 반복하는데 가로길이를 입력받은 N이 곧 열이 됨
            row_val = 1
            column_val = 1

            boolean = False # 2중 for문 탈출 위한 변수

            for rx, ry in dxy : # 가로로 긴 값 시작
                for row in range(1, M) : # 현재 위치 시점으로 행만큼 더함
                    row_nx = i + rx * row
                    row_ny = j + ry * row 

                    if 0 <= row_nx < M and 0 <= row_ny < N: # 배열 범위 안에서
                        if lst[row_nx][row_ny] == 0 : # 값이 0이라면 막대가 끝났다는 뜻이니 for문 종료
                            boolean = True # 2중 for문 탈출 위한 boolean
                            break
                        else :
                            row_val += 1 # 막대가 계속되면 1을 더함
                    else :
                        boolean = True
                        break

            for cx, cy in dxy : # 세로로 긴 값 시작, 위 for문과 동일
                for column in range(1, N) :
                    column_nx = i + cx * column
                    column_ny = j + cy * column

                    if 0 <= column_nx < M and 0 <= column_ny < N:
                        if lst[column_nx][column_ny] == 0 :
                            boolean = True
                            break
                        else :
                            column_val += 1
                    else :
                        boolean = True
                        break


            if row_val > result : # 더 큰 값 비교하여 result에 저장
                result = row_val
            elif column_val > result :
                result = column_val



    print(f'#{tc} {result}')

