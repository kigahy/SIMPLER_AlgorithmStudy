# 다음 강의가 이분 탐색을 이해하는 데 큰 도움이 되었다
# 기타 문제를 풀 때도 도움이 될 것으로 생각함
# https://www.youtube.com/watch?v=qR8dothNu1w
# 최종 값을 찾기 위해서는 mid 자체가 타깃이 될 때까지 반복하게 된다는 것을 알게 됨
# 따라서 답도 34행 maximum = mid 처럼 최종 변수에 mid 값 자체를 넣는 것임

N = int(input()) # 지방 수
arr = sorted(map(int, input().split())) # 예산요청
M = int(input()) # 총 예산

# 구하고자 하는 예산은 0원부터
start = 1
# 상한액은 150을 굳이 넘어가지 않음
end = max(arr)
# 출력할 최대 예산
maximum = 0

# 이진탐색 시작
while start <= end :
    total = 0                # 예산 합
    mid = (start+end) // 2   # 중앙값 선정

    # 이진탐색을 한번 할 때마다 각 요청의 예산만큼 반복
    for money in arr :
        # 중앙값보다 요청한 예산이 작다면 돈낭비 말고 요청한 금액만 줌
        total += min(money, mid)

    # 현재의 total 값이 예산 상한액을 초과했을 때
    # 답의 후보인 maximum도 바꾸어줌
    if total <= M :
        start = mid + 1
        maximum = mid

    # 이분탐색 결과 더 적은 값은 볼 필요도 없음
    else :
        end = mid - 1

print(maximum)