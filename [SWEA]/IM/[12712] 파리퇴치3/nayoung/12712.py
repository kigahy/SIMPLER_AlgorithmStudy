# SWEA. 12712  파리퇴치 3

'''
N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개체 수를 의미한다.

아래는 N=5 의 예이다.

파리 킬러 스프레이를 한 번만 뿌려 최대한 많은 파리를 잡으려고 한다.

스프레이의 노즐이 + 형태로 되어있어, 스프레이는 + 혹은 x 형태로 분사된다.

스프레이를 M의 세기로 분사하면 노즐의 중심이 향한 칸부터 각 방향으로 M칸의 파리를 잡을 수 있다.

다음은 M=3 세기로 스프레이르 분사한 경우 파리가 퇴치되는 칸의 예로, +또는 x 중 하나로 분사된다.

뿌려진 일부가 영역을 벗어나도 상관없다.

한 번에 잡을 수 있는 최대 파리수를 출력하라.


[제약 사항]

1. N 은 5 이상 15 이하이다.
2. M은 2 이상 N 이하이다.
3. 각 영역의 파리 갯수는 30 이하 이다.

[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고,
다음 N 줄에 걸쳐 N x N 배열이 주어진다.
'''

import sys
sys.stdin = open('input.txt', 'r')

def plus_kill(mosq):   # + 모양 kill
    dxy = [[0,1], [1,0], [0,-1], [-1,0]]  # 우 하 좌 상 방향 시계방향
    max_kill = 0

    for i in range(N):
        for j in range(N):
            kill = 0
            for dx, dy in dxy:
                for num in range(1,M):
                    nx = i + (dx*num)
                    ny = j + (dy*num)
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        continue
                    kill += mosq[nx][ny]
            kill += mosq[i][j]

            if max_kill < kill:  # max값 갱신
                max_kill = kill
    return max_kill


def mul_kill(mosq):  # X자 모양 kill
    dxy = [[-1, 1], [1, 1], [1, -1], [-1, -1]]  # 우 하 좌 상 방향 시계방향
    max_kill = 0

    for i in range(N):
        for j in range(N):
            kill = 0

            for dx, dy in dxy:
                for num in range(1,M):   # 세기크기만큼 원소 접근
                    nx = i + (dx * num)
                    ny = j + (dy * num)

                    if nx < 0 or nx >= N or ny < 0 or ny >= N:  # 인덱스 범위 초과 제외
                        continue
                    kill += mosq[nx][ny]
            kill += mosq[i][j]  # 현재 위치 원소 더해주기
            if max_kill < kill:
                max_kill = kill
    return max_kill

T = int(input())  # 테스트 케이스 수

for case in range(1,T+1):
    N, M = map(int,input().split())   # N 모기 배열 크기  , M = 분사 세기
    mosq = [list(map(int,input().split())) for _ in range(N)]  # 모기 배열

    max_kill = max(plus_kill(mosq), mul_kill(mosq))
    print(f'#{case} {max_kill}')