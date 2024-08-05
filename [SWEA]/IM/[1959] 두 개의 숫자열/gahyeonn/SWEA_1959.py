T = int(input())

for test_case in range(1, T+1) :
    small, big = map(int, input().split()) # 비교적 작은 리스트와 큰 리스트로 나누어 받음

    up = list(map(int, input().split())) # 작은 리스트는 위로
    down = list(map(int, input().split())) # 큰 리스트는 아래로

    if small > big : # small 변수값이 더 크다면 big과 small의 값 및 un과 down의 리스트도 바꿔줌
        big, small = small, big
        up, down = down, up
    elif small < big : # 크기가 알맞다면 pass
        pass

    max_val = 0
    for i in range(big-small+1) : # 밑에서 큰 리스트의 개수 - 작은 리스트의 개수 + 1 로 크기 맞춰줌
        
        val = 0
        for j in range(small) : # 위의 작은 리스트의 [0]부터 반복
            val += up[j] * down[i+j] # 주의! 작은 리스트 값과 작은 리스트의 위치에 맞춘 down이 맞물림
        if val > max_val : # 계산 값이 크다고 가정한 변수보다 크다면 max_val에 저장
            max_val = val
 
    print(f'#{test_case} {max_val}')
