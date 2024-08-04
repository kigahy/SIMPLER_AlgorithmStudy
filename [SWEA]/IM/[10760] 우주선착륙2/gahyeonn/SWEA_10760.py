T = int(input())

for test_case in range(1, T+1) :
    h, y = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(h)]

    di = [0, 1, 1, 1, 0, -1, -1, -1]
    dj = [1, 1, 0, -1, -1, -1, 0, 1]

    num = 0
    for i in range(h) :
        for j in range(y) :
            count = 0
            for k in range(8) :
                ni = i + di[k]
                nj = j + dj[k]

                if 0 <= ni < h and 0 <= nj < y :
                    if lst[ni][nj] < lst[i][j] :
                        count+=1
            if count >= 4 :
                num += 1
    print(f'#{test_case} {num}')




    
    
    

