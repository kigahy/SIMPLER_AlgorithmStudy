import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    dxy = [[0,0], [0,1], [0,-1], [1,0], [-1,0]]

    max_v = 0

    for i in range(N):
        for j in range(M):
            sum_v = 0
            for k in range(5):
                
                # N,M 범위 조심!!!!!!!
                if i+dxy[k][0] >= 0 and i+dxy[k][0] < N and j+dxy[k][1] >= 0 and j+dxy[k][1] < M:
                    sum_v += arr[i+dxy[k][0]][j+dxy[k][1]]
            
            if max_v < sum_v:
                max_v = sum_v

    print(f'#{test_case} {max_v}')



