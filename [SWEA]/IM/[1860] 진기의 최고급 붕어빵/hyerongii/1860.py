# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    # N:사람 수 M:걸리는 시간(초) K: 붕어빵 수
    N, M, K = map(int, input().split())
    # 사람 방문 시간 리스트
    customer_lst = list(map(int, input().split()))
    # 방문사람들 중에 가장 늦은 사람 뽑아내려고 sort
    customer_lst.sort()
    # 사람들 중에서 가장 방문 시간 늦은 사람으로 붕어빵 수 만들기
    # 시간을 인덱스로 고려하기
    max_c = customer_lst[-1]
    boongs = [0] * (max_c+1)
    for time in range(1, max_c+1):
        # M초 마다 K개 만큼 생성 쭉 이어져 가야해서 몫으로 생각해주기
        # ex/ 2초에 2개 만들면 0 0 2 2 4 4 ... 이런식으로 만들어줌
        boongs[time] += K*(time//M)
    result = "Possible"
    for customer in customer_lst:
        # 방문객 오는 시간에 붕어빵 있으면 붕어빵 개수 차감
        if boongs[customer] >= 1:
            for boong in range(customer, max_c+1):
                boongs[boong] -= 1
        # 방문객 오는 시간에 붕어빵이 없으면
        else:
            result = "Impossible"
            break
    print(f'#{tc} {result}')

