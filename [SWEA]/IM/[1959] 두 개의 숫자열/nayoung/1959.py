# SWEA 1959 두 개의 숫자열

'''
N 개의 숫자로 구성된 숫자열 Ai (i=1~N) 와 M 개의 숫자로 구성된 숫자열 Bj (j=1~M) 가 있다.

아래는 N =3 인 Ai 와 M = 5 인 Bj 의 예이다.

Ai = 1 5 3
Bi = 3 6 -7 5 4

Ai 나 Bj 를 자유롭게 움직여서 숫자들이 서로 마주보는 위치를 변경할 수 있다.

단, 더 긴 쪽의 양끝을 벗어나서는 안 된다.

Ai =       1  5  3
bj = 3  6 -7  5  4

서로 마주보는 숫자들을 곱한 뒤 모두 더할 때 최댓값을 구하라.

위 예제의 정답은 아래와 같이 30 이 된다.

Ai =      1  5  3
Bj = 3  6 -7 5  4


[제약 사항]

N 과 M은 3 이상 20 이하이다.


[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고,

두 번째 줄에는 Ai,

세 번째 줄에는 Bj 가 주어진다.

[출력]

출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
'''

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())  # 테스트 케이스 수 T


def max_case(a, b):  # max 함수
    if a > b:
        return a
    return b


def min_case(x, y):  # min 함수
    if x > y:
        return y
    return x


for case in range(1, T + 1):
    N, M = map(int, input().split())   # N, M개의 숫자 입력 받음
    Ai = list(map(int, input().split()))
    Bi = list(map(int, input().split()))

    max_hap = 0  # 최대 합
    for i in range(max_case(N, M) - min_case(N, M) + 1):  # N-M+1 만큼 순회
        zero_arr = [0] * max_case(N, M)  # 0인 빈배열 만듦

        for j in range(min_case(len(Ai), len(Bi))):
            if len(Ai) > len(Bi):  # 길이 짧은 배열 빈 배열 값 대입
                zero_arr[i + j] = Bi[j]   # 빈 배열 순회하면서 길이 짧은 원소 값 할당
            else:
                zero_arr[i + j] = Ai[j]
        hap = 0  # zero_arr 순회하면서 마주보고있는 원소와 곱해서 나온 합 담을 값

        for k in range(max_case(N, M)):
            if len(Ai) > len(Bi):
                hap += zero_arr[k] * Ai[k]
            else:
                hap += zero_arr[k] * Bi[k]
        if max_hap < hap:  # max값 재할당
            max_hap = hap
    print(f'#{case} {max_hap}')