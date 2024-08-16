import sys
sys.stdin = open("input.txt", "r")

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 열탐색 기준으로 작은열에 1 큰열에 2 이렇게 오는 개수 세기
    # 주어진 행렬 뒤집는게 count 할 때 편할듯
    count = 0
    real_arr = [[0]*N for _ in range(N)]

    # 행이랑 열 스위치
    for i in range(N):
        for j in range(N):
            real_arr[i][j] = arr[j][i]

    for i in range(N):
        # 스택 사용해서 stack 끝 값이 1이고 2가 오면 count 세기
        stack = []
        for j in range(N):
            if real_arr[i][j] == 1:
                stack.append(1)
            elif real_arr[i][j] == 2:
                if stack and stack[-1] == 1:
                    stack.append(2)
                    count += 1

    print(f'#{tc} {count}')

