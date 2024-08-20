# SWEA. 10580. [전봇대]

T = int(input())

for case in range(1, T+1):
    N = int(input())  # 전선 갯수
    pole_AB = [list(map(int,input().split())) for _ in range(N)]   # 전봇대 선 AB
    res = 0
    for i in range(N-1):
        for j in range(i+1,N):
            if pole_AB[i][0] < pole_AB[j][0] and pole_AB[i][1] > pole_AB[j][1]:  # A1 < A2 일 때  B1 > B2 교차 생성
                res += 1
            elif pole_AB[i][0] > pole_AB[j][0] and pole_AB[i][1] < pole_AB[j][1]: # A1 > A2 일 때  B1 < B2 교차 생성
                res+=1
    print(f'#{case} {res}')