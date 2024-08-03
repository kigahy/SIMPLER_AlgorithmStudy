'''
착륙지는 ij [0,0]
예비후보지
[-1,-1] [-1,0] [-1,1] 
[0,-1]          [0,1] 
[1,-1] [1,0] [1,1] 
이중에서 [0,0] 보다 값이 낮은 지점이 4개 이상이어야함

이것을 만족하는 후보지의 수 찾기
'''

import sys
sys.stdin = open("input.txt", "r")

dxy = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0

    for i in range(N):
        for j in range(M):
            count = 0
            for k in range(8):
                if i+dxy[k][0] >= 0 and i+dxy[k][0] < N and j+dxy[k][1] >= 0 and j+dxy[k][1] < M:
                    if arr[i][j] > arr[i+dxy[k][0]][j+dxy[k][1]]:
                        count += 1
            if count >= 4:
                result += 1

    print(f'#{test_case} {result}')