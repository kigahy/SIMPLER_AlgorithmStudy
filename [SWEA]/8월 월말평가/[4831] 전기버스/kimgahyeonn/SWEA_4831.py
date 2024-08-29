# 시행착오를 겪고 챗GPT가 짜준 코드를 채택하였습니다.
# 맨 처음 검색한 자료. 직관적이고 간단함 https://hyunse0.tistory.com/244

T = int(input())

for tc in range(1, T + 1):
    K, N, M = map(int, input().split())  # 이동거리, 종점(정류장 수), 충전기 수
    charge = list(map(int, input().split()))  # 충전소 위치 리스트
    
    count = 0  # 충전한 횟수
    distance = 0  # 현재 위치
    energy = K  # 현재 에너지 (최대 이동 거리)
    
    while distance < N:
        # 현재 위치에서 갈 수 있는 최대 거리
        if distance + energy >= N: # 나는 distance > N 으로만 생각하였음. + energy 기억할 것
            distance = N
            break
        
        # 현재 위치에서 이동할 수 있는 최대 거리까지 충전소를 찾아야 함
        next_stop = distance
        for i in range(distance + 1, min(distance + energy + 1, N + 1)): # 이런거 어려움
        # 현재 지점의 다음 지점부터 시작. 현재 거리부터 에너지로 갈 수 있는 곳 혹은 마지막 인덱스 중 적은 것만큼 반복 (인덱스 벗어나지 않기 위하여)
            if i in charge: # 충전소를 발견했다면 다음 지점을 충전소의 위치로
                next_stop = i
        
        if next_stop == distance:
            # 더 이상 이동할 수 없는 경우
            count = 0
            break
        
        # 충전소에 도착한 경우
        if next_stop in charge:
            count += 1
            energy = K  # 에너지를 다시 충전
        distance = next_stop # 한번 반복할 때마다 거리는 지정된 다음 위치로 됨
        energy -= (next_stop - distance) # 이동한 거리만큼 에너지 계산
    
    print(f'#{tc} {count}')

        
    '''시행착오. 종료조건이 명확하지 않아서인가?
    for i in range(N) : # 0부터 총 종점까지 하나씩 순회
        if distance >= N : # 이동한 거리가 종점보다 크다면 도착했다는 말이므로 종료함
            break
        if distance < i : # 실제 이동 거리가 충전기를 찾는 거리 i보다 적다면
            count = 0 # 차 멈췄으니까 반복문 종료
            break
        if i in charge and distance == i : # 종점까지 가는 거리에 충전기가 있고, 이 충전기의 위치와 실제 이동거리가 일치한다면
            distance = i + K
            count += 1
        elif distance > i : # 실제 이동 거리가 가야하는 거리 i보다 크다면
            continue # 충전 안해도 되고 다음 i로 넘어감.    
    '''
    
''' 시행착오2 어줍잖게 while 시도했다가 망함
for tc in range(1, T+1) :
    K, N, M = map(int, input().split()) # 이동거리, 종점(정류장 수=), 충전기 수
    charge = list(map(int, input().split()))
    count = 0 # 충전한 횟수
    distance = 0 # 실제 이동 거리
    energy = K # 이동할 수 있는 힘

    while distance > N : # 이동 거리가 N 이상이 되면 종료
        distance += 1 # 현재 거리 1 증가
        energy -= 1 # 힘 1 감소

        if distance in charge : # 현재 충전소에 도착하였다면
            distance += K # 거리 증가
            energy += K # 힘도 증가

        
        if energy == 0 :
            count = 0
            break

        distance += 1

    print(distance)

    print(f'#{tc} {count}')

    '''