'''
string으로 접근하여 푼 방법
'''

import sys
sys.stdin = open('input.txt', 'r')

for case in range(1, 11):
    length = int(input())
    arr = [list(input().split()) for _ in range(length)]  # 100X100 배열 입력
    deadlock = 0   # 교착 갯수 담아줄 변수 초기값 설정

    for col in range(length):  # 열방향으로 row 순회
        str = ''
        for row in range(length):
            if arr[row][col] !='0':   # 0을 제외한 숫자를 string을 들고옴
                str += arr[row][col]   # 예 ) 1번째 열 : '1' / 3번째 열 : '2121'

        deadlock += str.count('12')   # '12' 순이면 교착 상태임을 알 수 있음 /   '112'이어도 교차 상태는 1개임
                                        # 각 열 순회하면서 12순이면 교착상태이니 카운트해줌
    print(f'#{case} {deadlock}')
