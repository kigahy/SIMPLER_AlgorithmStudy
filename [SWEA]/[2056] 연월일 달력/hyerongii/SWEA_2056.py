# import sys
# sys.stdin = open("input.txt", "r")

'''
연월일 순으로 구성된 8자리의 날짜가 입력으로 주어진다.
22220228 -> 2222/02/28

해당 날짜의 유효성을 판단한 후, 날짜가 유효하다면
[그림1] 과 같이 ”YYYY/MM/DD”형식으로 출력하고,
날짜가 유효하지 않을 경우, -1 을 출력하는 프로그램을 작성하라.

연월일로 구성된 입력에서 월은 1~12 사이 값을 가져야 하며
일은 [표1] 과 같이, 1일 ~ 각각의 달에 해당하는 날짜까지의 값을 가질 수 있다.

[입력]
입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
다음 줄부터 각 테스트 케이스가 주어진다.


[출력]
출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
'''

T = int(input())

for test_case in range(1, T+1):

    # split 함수는 list로 묶어주는 기능 있기 때문에 원소 받아서 문자열 하나하나로 풀어주는 작업 진행
    input_data = list(input().split()[0])

    # 입력 받은 숫자를 순서대로 연,월,일로 나누어줌
    # 이때 str 타입 이므로 쪼개진 str을 합치는 join 사용
    year = ''.join(input_data[0:4])
    month = ''.join(input_data[4:6])
    date = ''.join(input_data[6:8])

    # 28,30,31일인 월의 리스트 만들기
    month_30 = ['04', '06', '09', '11']
    month_31 = ['01', '03', '05', '07', '08', '10', '12']
    month_28 = ['02']

    # 월 먼저 조건에 넣고 아닐시 -1 프린트
    if (1 <= int(month)) & (int(month) <= 12):
        if (month in month_28) & (int(date) <= 28):
            print(f'#{test_case} {year}/{month}/{date}')   
        elif (month in month_30) & (int(date) <= 30):
            print(f'#{test_case} {year}/{month}/{date}')
        elif (month in month_31) & (int(date) <= 31):
            print(f'#{test_case} {year}/{month}/{date}')
        else :
            print(f'#{test_case} -1')
    else :
        print(f'#{test_case} -1')
