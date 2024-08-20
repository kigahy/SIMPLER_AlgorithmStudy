# SWEA 9489. [고대 유적]


'''
땅속의 구조물을 촬영할 수 있는 특수 위성 카메라에 땅속에 묻힌 고대 구조물이 발견되었다.

구조물은 폭 1m, 길이 2m 이상의 직선 형태로 서로 평행 또는 직각으로만 자리하고 있으며,
1mx1m의 해상도의 사진데이터에 구조물이 있는 자리는 1로 나타난다.

사진의 해상도는 NxM이며, 구조물이 있는 곳은 1, 빈 땅은 0으로 표시된다.

위 그림의 경우 가장 긴 구조물은 노란색으로 표시된 영역이며, 길이는 6이다.

교차하거나 만나는 것처럼 보이는 구조물은 서로 다른 깊이에 묻힌 것이므로 직선인 구조물만 고려하면 된다.

다음과 같은 경우는 길이가 3인 구조물 4개가 겹쳐 보이는 것이다.

평행한 모든 구조물은 서로 1m이상 떨어져 있고, 구조물의 최소 크기는 1x2m이다.

여러 구역의 사진 데이터가 주어질 때, 각 구역 별로 가장 긴 구조물의 길이를 찾는 프로그램을 만드시오.

입력

첫 줄에 사진 데이터의 개수, 다음 줄부터 사진 데이터 별로 첫 줄에 N과 M, 이후 N개의 줄에 M개씩의 데이터가 제공된다.

(3<=N, M<=100)

출력

#과 1번부터 시작하는 사진 번호, 빈칸과 가장 긴 구조물의 길이를 출력한다

'''
T = int(input())  # 테스트 케이스 수

dxy = [[1,0],[0,1]]  # 우, 하

for case in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]  # NXM 배열 입력
    res = 0

    for row in range(N):
        for col in range(M):
            if not arr[row][col]:  # 유물없음
                continue
            for dx, dy in dxy:
                cnt = 1  # 유물이 있다는거
                for k in range(1, max(N,M)):   # N,M이 뭐가 큰지 모르기때문에 둘 중 max값 가져옴
                    nx, ny = row + dx*k , col + dy*k
                    if nx < 0  or nx >= N or ny < 0 or ny >= M or arr[nx][ny] == 0:  # 범위 벗어나거나 유물이 없거나
                        break
                    if arr[nx][ny]:  # 유물있으면 유물갯수 더해줌줌
                        cnt+=1
                if res < cnt:   # 최대값 갱신
                    res = cnt

    print(f'#{case} {res}')