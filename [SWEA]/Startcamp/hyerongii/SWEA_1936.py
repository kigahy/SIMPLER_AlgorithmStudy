'''
A와 B가 가위바위보를 하였다.
가위는 1, 바위는 2, 보는 3으로 표현되며 A와 B가 무엇을 냈는지 입력으로 주어진다.
A와 B중에 누가 이겼는지 판별해보자. 단, 비기는 경우는 없다.

[입력]
입력으로 A와 B가 무엇을 냈는지 빈 칸을 사이로 주어진다.
3 2

[출력]
A가 이기면 A, B가 이기면 B를 출력한다.
A
'''

input_data = input()
a, b = input_data.split()
num_a = int(a)
num_b = int(b)

if (num_a > num_b):
    if (num_a-num_b == 1):
        print("A")
    else :
        print("B")
elif (num_b > num_a):
    if (num_b-num_a == 1):
        print("B")
    else :
        print("A")