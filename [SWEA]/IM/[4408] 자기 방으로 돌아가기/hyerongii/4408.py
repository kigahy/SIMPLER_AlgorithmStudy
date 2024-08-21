# import sys
# sys.stdin = open("input.txt", "r")

# 문제 이해를 잘 못했다.. 마주보는 곳으로 갈때 안 겹친다고 생각했었다ㅠㅠ
# 구글의 힘을 빌려 다시 풀어보았다..

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    # 사용 중인 복도를 표시할 리스트
    corridor = [0] * 200

    # 복도를 기준으로 학생이 통과하여 지나가면 그 인덱스의 값 카운팅
    '''
    room     1 3 5 7 ... 399
    corridor 0 1 2 3 ... 199
    room     2 4 6 8 ... 400
    '''
    for n in range(N):
        # 시작방 번호, 끝방 번호 리스트로 받아서 저장
        temp = list(map(int, input().split()))
        for i in range(2):
            # 복도 인덱스로 변환
            # 방 번호가 짝수면 
            if temp[i] % 2:
                temp[i] = (temp[i] - 1) // 2
            # 홀수면 
            else:
                temp[i] = (temp[i] - 2) // 2
        # 뒷 방 번호가 더 크면 복도 지나가는 인덱스에 값 더해주기
        if temp[0] <= temp[1]:
            for j in range(temp[0], temp[1]+1):
                corridor[j] += 1
        # 더 작을 때
        else:
            for j in range(temp[1], temp[0]+1):
                corridor[j] += 1

    # 가장 많이 복도 인덱스가 카운팅된 수를 출력하면, 그 복도를 동시에 사용할 수 없는 횟수이기 때문에 정답
    print(f'#{tc} {max(corridor)}')

