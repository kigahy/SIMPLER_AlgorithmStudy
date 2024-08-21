# import sys
# sys.stdin = open("input.txt", "r")

# A 증가할 때 B 감소/ B 증가할 때 A감소 이면 점 하나씩 생긴다는 규칙은 찾았으나 구현할 때 잘못생각해주어서
# list 안 만들고 바로 받아서 처리 하려다 보니 구현 힘들었음
# 다른 사람이 푼 방법보고 해결함

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = 0
    lst = []
    for _ in range(N):
        # 입력 잘 받아주기
        A, B = map(int, input().split())
        # A가 증가할 때, B 감소면 +1// B 증가할 때, A 감소면 +1
        if lst:
            for a, b in lst:
                if (a < A and b > B) or (a > A and b < B):
                    result += 1
        lst.append((A, B))
    print(f'#{tc} {result}')

# 실패한 방법.. 
# max_A = 1
# max_B = 1
# if max_A <= A:
#     max_A = A
#     if max_B > B:
#         result += 1
#     else:
#         max_B = B
# else:
#     if max_B <= B:
#         result += 1
#     else:
#         max_B = B