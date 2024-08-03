# import sys
# sys.stdin = open("input.txt", "r")

'''
10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라.
(소수점 첫째 자리에서 반올림한 정수를 출력한다.)

[제약 사항]
각 수는 0 이상 10000 이하의 정수이다.

[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.

[출력]
출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
'''

T = int(input())

for test_case in range(1, T+1):

    # 10개의 수를 입력받은 줄 각각 int 형변환 후 리스트로 묶음
    input_data = list(map(int, input().split())) 
    
    sum = 0
    
    # 10개로 동일하지만 추후 길이 바뀔경우 대비해서 len 사용
    len_input_data = len(input_data)  
    
    for j in range(len_input_data):
        
        # 리스트 내 값 다 더하기
        sum += input_data[j] 
    
    # 리스트 내 다 더한 합을 값 개수로 나누고 소수점 첫째 자리에서 반올림
    avg = round(sum/len_input_data)
    print(f'#{test_case} {avg}')