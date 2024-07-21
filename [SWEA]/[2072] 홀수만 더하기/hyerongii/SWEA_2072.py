# import sys
# sys.stdin = open("input.txt", "r")

'''
10개의 수를 입력 받아, 
그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라.

입력-
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.

출력-
출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
'''

T = int(input())

for test_case in range(1, T+1):
    input_data = list(map(int, input().split()))
    
    odd_sum = 0

    for j in range(len(input_data)):

        # 리스트 내 값의 나머지가 1이면 : 홀수이면 
        if input_data[j] % 2 == 1:

            # 값을 합에 더하기
            odd_sum += input_data[j]
            
    print(f'#{test_case} {odd_sum}')
