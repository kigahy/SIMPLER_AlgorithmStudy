# SWEA 16268. 풍선팡2

'''
종이 꽃가루가 들어있는 풍선이 NxM 크기의 격자판에 붙어있는데, 어떤 풍선을 터뜨리면 상하좌우의 풍선이 추가로 터진다고 한다.

다음의 경우 가운데 풍선을 터뜨리면 상하좌우의 풍선이 추가로 1개씩 터지면서 총 5개의 꽃가루가 날리게 된다.

NxM개의 풍선에 들어있는 종이 꽃가루 개수A가 주어지면,
한 개의 풍선을 선택해 터뜨렸을 때 날릴 수 있는 꽃가루 수 중 최대값을 출력하는 프로그램을 만드시오.

(3<=N, M<=100)



[입력]

첫 줄에 테스트케이스 수 T, 다음 줄부터 테스트케이스 별로 첫 줄에 N과 M,
이후 N줄에 걸쳐 M개씩 풍선에 든 종이 꽃가루 개수가 주어진다.



[출력]

#과 테스트케이스 번호, 빈칸에 이어 종이 꽃가루의 최대 개수를 출력한다.

'''

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())  # 테스트 케이스 수

di = [0, 0, 1, 0, -1]  # 우, 본인, 하, 좌, 상 좌표지정
dj = [1, 0, 0, -1, 0]

for case in range(1, T + 1):
    N, M = map(int, input().split())  # N 행 M열 입력받음
    arr = [list(map(int, input().split())) for _ in range(N)]  # 입력받은 2중 배열
    max_pang = 0  # 최댓값 초기 설정

    for i in range(N):
        for j in range(M):
            pang = 0  # 각 원소의 반복문 돌때마다 pang 초기값 설정
            for k in range(5):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:  # 벗어나는 범위 지정 막음
                    pang += arr[ni][nj]
            if max_pang < pang:  # max값 갱신
                max_pang = pang
    print(f'#{case} {max_pang}')