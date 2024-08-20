'''
방이 홀수번 (1~399)방 짝수번(2~400)방 으로 나눠져있는데
한 방(201개의 방)으로 합쳐서 1,2 번 방을 같은 인덱스로 가지게 하여 같은 방에 들어가게끔 풀이
'''

T = int(input())  # 테스트 케이스 수

for case in range(1, T+1):
    N = int(input())  # 돌아가야 할 학생들의 수

    room = [list(map(int,input().split())) for _ in range(N)]

    r = [0] * 201  # 방 1번부터 200번까지

    for A,B in room:
        start = (min(A,B)+1)//2  # 방번호가 홀수 짝수여도 같은 인덱스에 집어넣기 위함
        end = (max(A,B)+1) // 2
        for i in range(start, end+1):   # start부터 end까지 모두 다녀갔다 가정
            r[i] += 1

    print(f'#{case} {max(r)}')