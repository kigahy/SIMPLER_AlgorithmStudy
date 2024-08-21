# import sys
# sys.stdin = open("input.txt", "r")

# 먼저 1 x 길이 중에서 제일 긴 값 찾아야 하니
# 행탐색으로 먼저 찾아주고 전치행렬만들어줘서 열탐색으로 찾아주는 방법 사용
# 전치행렬 만들어서 탐색하는 방법이 너무 편하고 직관적이어서 자주 사용하게됨 ㅠㅠ (시간복잡도나 소요시간에선 안좋을듯)

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    pic = [list(map(int, input().split())) for _ in range(N)]
    # 행렬 탐색하면서 연속으로 1 오면 카운트 하기 (행 우선 탐색)
    max_len = 0
    for i in range(N):
        count_r = 1
        for j in range(M - 1):
            if pic[i][j] == 1 and pic[i][j + 1] == 1:
                count_r += 1
        if max_len < count_r:
            max_len = count_r
    # 전치행렬 만들어줌
    rev_arr = [[0] * N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            rev_arr[i][j] = pic[j][i]
    # 다시 탐색해서 카운트
    for i in range(M):
        count_c = 1
        for j in range(N - 1):
            if rev_arr[i][j] == 1 and rev_arr[i][j + 1] == 1:
                count_c += 1
        if max_len < count_c:
            max_len = count_c
    print(f'#{tc} {max_len}')