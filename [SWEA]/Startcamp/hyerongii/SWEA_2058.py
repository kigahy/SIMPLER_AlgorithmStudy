'''
[제약 사항]
자연수 N은 1부터 9999까지의 자연수이다. (1 ≤ N ≤ 9999)

[입력]
입력으로 자연수 N이 주어진다.
6789

[출력]
각 자릿수의 합을 출력한다.
30
'''

input_data = int(input())

data_sum = 0
while input_data>0:
    b=input_data%10
    input_data//=10
    data_sum+=b

print(data_sum)