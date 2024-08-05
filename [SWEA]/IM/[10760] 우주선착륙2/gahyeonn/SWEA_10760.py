T = int(input())

for test_case in range(1, T+1) :
    h, y = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(h)]

    di = [0, 1, 1, 1, 0, -1, -1, -1] # 델타 분석을 활용한 접근
    dj = [1, 1, 0, -1, -1, -1, 0, 1] # di dj는 내 위치를 기준으로 행 열

    num = 0
    for i in range(h) :
        for j in range(y) :
            count = 0
            for k in range(8) :
                ni = i + di[k] # 전체 배열을 기준으로 행과 열을 찾는 ni nj 변수
                nj = j + dj[k]

                if 0 <= ni < h and 0 <= nj < y :
                    if lst[ni][nj] < lst[i][j] : # lst[ni][nj]는 타깃의 위치가 가진 값, lst[i][j]는 내 위치
                        count += 1 # 내 위치가 가진 값보다 작으면 수를 셈
            if count >= 4 : # 수를 센 것이 4보다 크다면 최종 자리로 확정하여 num에 추가
                num += 1
    print(f'#{test_case} {num}')




    
    
    

