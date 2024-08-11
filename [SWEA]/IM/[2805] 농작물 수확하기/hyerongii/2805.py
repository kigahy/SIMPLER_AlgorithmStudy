import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

# N = 1         [0][0]

#               [0][1]             0 1:2
# N = 3  [1][0] [1][1] [1][2]      1 0:3
#               [2][1]             2 1:2

# N = 5          [0][2]                  0 2:3
#         [1][1] [1][2] [1][3]           1 1:4
#  [2][0] [2][1] [2][2] [2][3] [2][4]    2 0:5  여기이후 줄어듬
#         [3][1] [3][2] [3][3]           3 1:4
#                [4][2]                  4 2:3

    center = N//2  #centerj 열의 센터
    sum_v = 0

    for i in range(N):  # 0 1 2 3 4
        if i <= center: # 센터까지 늘어남
            sum_v += sum(arr[i][center-i:center+i+1])
        else:
            sum_v += sum(arr[i][i-center:N-(i-center)])

    print(f'#{tc} {sum_v}')


