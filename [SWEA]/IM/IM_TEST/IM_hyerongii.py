T = int(input())
for tc in range(1, T+1):
    # LED 랑 버튼의 수
    N = int(input())
    # 원하는 LED 패턴
    pattern = list(map(int, input().split()))
    # 패턴의 버튼(인덱스)가 몇의 배수인지 체크해서 돌리기
    # while로 패턴 만들어지면 break 하고 카운트 한 값 프린트

    # 0인 led 만들고
    LED = [0] * N
    count = 0
    # 1이 처음으로 오는 인덱스 뽑기 -> 여기부터 몇의 배수인지 check
    for i in range(N):
        if pattern[i] == 1 - LED[i]:
            start = i+1
            # 몇의 배수인지 찾았으니까 led 변화시키기
            count += 1
            for j in range(1, N+1):
                if j % start == 0:
                    LED[j-1] = 1 - LED[j-1]

    print(f'#{tc} {count}')



'''
5
5
1 1 0 0 1
6
0 1 1 1 0 0
7 
1 1 1 1 1 1 1 
10
0 1 0 1 0 1 0 1 0 1
20 
0 0 0 0 1 0 0 1 0 1 0 1 0 1 0 1 1 1 0 0 

'''