'''
연월일 순으로 구성된 8자리의 날짜가 입력으로 주어진다.
해당 날짜의 유효성을 판단한 후, 날짜가 유효하다면
"YYYY/MM/DD"형식으로 출력하고,
날짜가 유효하지 않을 경우, -1을 출력하는 프로그램을 작성하라.

연월일로 구성된 입력에서 월은 1~12 사이 값을 가져야 하며
일은 각각의 달에 해당하는 날짜까지의 값을 가질 수 있다.
- 2월의 경우, 28일인 경우만 고려한다.

[입력]
입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
다음 줄부터 각 테스트 케이스가 주어진다.

[출력]
테스트 케이스 t에 대한 결과는 '#t'을 찍고, 한 칸 띄고, 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
'''

T = int(input())
# 입력받을 날짜 수를 T로 설정

for i in range(T):
    data = input()
    data_y = int(data[:4])      # 인덱스를 사용하여 날짜의 연도를 추출하여 저장
    data_m = int(data[4:6])     # 날짜의 월 추출
    data_d = int(data[6:])      # 날짜의 일 추출
    if data_m == 1 or data_m == 3 or data_m == 5 or data_m == 7 or data_m == 9 or data_m == 11:
        if data_d >= 1 and data_d <= 31:
            print(f'#{i+1} {data[:4]}/{data[4:6]}/{data[6:]}')
        else:
            print(f'#{i+1} -1')
    elif data_m == 4 or data_m == 6 or data_m == 8 or data_m == 10 or data_m == 12:
        if data_d >= 1 and data_d <= 30:
            print(f'#{i+1} {data[:4]}/{data[4:6]}/{data[6:]}')
        else:
            print(f'#{i+1} -1')
    elif data_m == 2:
        if data_d >= 1 and data_d <= 28:
            print(f'#{i+1} {data[:4]}/{data[4:6]}/{data[6:]}')
        else:
            print(f'#{i+1} -1')
    else:
        print(f'#{i+1} -1')
# 숫자가 변환될 달력의 범위를 지정하고 그에 맞지 않으면 -1을 출력하도록 반복문과 조건문 설정