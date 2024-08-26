import sys
sys.stdin = open("input.txt", "r")

# K 만큼 이동할 수 있음 그때 충전기 찾기
# 충전기 없으면 그 전 충전기 있는 곳으로 가서 충전하고 카운트
# 다시 이동 반복

def count_charge():
    stop = 0
    while True:
        # busstop K배수 만큼 돌기
        stop += K

        # 만약 끝까지 정류장 끝 이상까지 이동했다면
        if stop >= N:
            # 충전한 횟수 다 더해서 반환
            return sum(bus_stop)
        
        # tmp로 현재 멈춘 정거장 번호 저장후에 돌아가서 찾을 때 stop까지 다시 돌아가기 위해서 tmp 변수 만들어줌 
        tmp = stop
        # chargestop 아니면 돌아가서 찾기
        while stop not in charge_stop:
            # 왼쪽으로 이동하는데 K까지 이동해서 없으면
            stop -= 1
            if stop == tmp-K:
                # 0 반환
                return 0
        # 충전한 곳 카운트
        bus_stop[stop] += 1

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charge_stop = list(map(int, input().split()))
    # 0~N 버스정류장, 충전하면 그 정류장의 인덱스에 수 할당하기 위해서
    bus_stop = [0]*(N+1)
    print(f'#{tc} {count_charge()}')




