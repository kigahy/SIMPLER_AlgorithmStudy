T = int(input())

for test_case in range(1, T+1) :
    h, y = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(h)]

    di = [0, 0, 1, 0, -1]
    dj = [0, 1, 0, -1, 0]
    maxi = 0

    for i in range(h) :
        for j in range(y) : 
            total = 0
            for k in range(5) :
                ni = i + di[k]
                nj = j + dj[k]

                s = 0
                if 0 <= ni < h and 0 <= nj < y :
                    s += lst[ni][nj]
                total += s 
                
                if maxi < total :
                    maxi = total

    print(f'#{test_case} {maxi}')

