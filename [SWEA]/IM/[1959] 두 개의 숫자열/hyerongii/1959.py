import sys
sys.stdin = open("input.txt", "r")

def finding_max_sum(max_l, min_l):
    max_sum = 0
    for i in range(len(max_l)-len(min_l)+1):
        sum_v = 0
        for j in range(len(min_l)):
            sum_v += (min_l[j] * max_l[i+j])
        if max_sum < sum_v:
            max_sum = sum_v
    return max_sum

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    max_sum = 0

    # A랑 B크기 비교 작은쪽을 window
    if N > M:
        max_lst = A
        min_lst = B
        max_sum = finding_max_sum(max_lst, min_lst)
    elif N == M:
        for i in range(N):
            max_sum += A[i] * B[i]
    else :
        max_lst = B
        min_lst = A
        max_sum = finding_max_sum(max_lst, min_lst)
    
    print(f'#{test_case} {max_sum}')
