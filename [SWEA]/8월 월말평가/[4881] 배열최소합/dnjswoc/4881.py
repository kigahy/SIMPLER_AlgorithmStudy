# 17:30 -
import sys
sys.stdin = open('input.txt', 'r')

'''
저는 배열최소합 문제를 n-queen 문제와 비슷하게 풀었습니다.
먼저 첫 행의 열을 반복하면서 한 칸을 고르고, 그 자리를 놓을 수 있다고 판단되면
행 인덱스를 1 더하고, 방문표시를 하며 재귀함수를 사용합니다.
그렇게 다음 행으로 가 다시 열을 반복하면서 놓을 수 있는지 판단하는 방법을 반복해 조합을 완성합니다.
재귀를 반복하여 행이 N이 되면 조합이 완성된 것이므로 방문 표시가 된 자리의 인덱스를 
원래 2차원 배열에 대입하여 조합의 합을 구하고, 리스트에 저장합니다.
그 후 리스트에서 가장 작은 합을 출력하여 문제를 풀었습니다.
'''

T = int(input())


def is_valid(row, col, visited):    # 놓을 수 있는 자리인지 확인하는 함수
    for i in range(row):
        for j in range(N):
            if visited[i][j] == 1 and j == col:  # i행, j열에 방문한 적 있고, 놓을 열의 위치가 j라면
                return False    # return False
    else:
        return True     # for문을 다 돌아도 앞에 놓았던 열과 겹치지 않는다면 return True


def find_combination(row, mat, visited, sum_mat):   # 배열 조합을 찾을 함수
    if row == N:
        sum_arr = 0
        for i in range(N):
            for j in range(N):
                if visited[i][j] == 1:  # 방문한 적 있는 위치라면
                    sum_arr += mat[i][j]    # 그 위치의 숫자들의 합을 구함
        sum_mat.append(sum_arr)  # 숫자들의 합을 sum_mat 리스트에 저장
        return sum_mat

    for col in range(N):    # 열을 순회하면서
        if is_valid(row, col, visited):  # 놓을 수 있는 위치이면
            visited[row][col] = 1   # 방문 표시하고
            find_combination(row + 1, mat, visited, sum_mat)    # 다음 행으로 넘어감
            visited[row][col] = 0   # 방문 표시 지우기


for test_case in range(T):
    N = int(input())
    num_matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]   # 2차원 배열의 0리스트 생성
    sum_matrix = []     # 각 조합마다의 합을 기록하는 리스트
    find_combination(0, num_matrix, visited, sum_matrix)
    print(f'#{test_case + 1} {min(sum_matrix)}')