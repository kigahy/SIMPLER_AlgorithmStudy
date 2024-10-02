# 정해진 총액 이하에서 가능한 한 최대의 총 예산을 다음과 같이 배정

# 1. 모든 요청이 배정될 수 있는 경우. 요청한 금액 그대로 배정
# 2. 모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정한다.
# 상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정한다.

# 시간 초과 ;; ㅠㅠ
def find_sum(lst):
    # 가장 큰 값을 1씩 내려주기..
    # 더해서 상한액 나오면 리턴
    while True:
        if sum(lst) < M:
            return lst
        lst.sort()
        max_v = lst[-1]-1
        lst.pop()
        lst.append(max_v)

N = int(input())
budget_lst = list(map(int, input().split()))
M = int(input())

# 하나씩 더해가면서 이진탐색으로 생각해주기
# 먼저 정렬
budget_lst.sort()

# 만약 상한액 이하면 그냥 출력
if sum(budget_lst) <= M:
    result = max(budget_lst)
else:
    lst = budget_lst
    result = max(find_sum(lst))

print(result)