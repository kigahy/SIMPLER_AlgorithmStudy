# SWEA. 9367 점점 커지는 당근의 개수

'''
영준이는 당근 크기 선별기를 이용해 수확한 순서대로 당근의 크기를 기록하였다. 이 당근 선별기에는 특별한 기능이 있는데 연속으로 당근의 크기가 커진 경우 그 개수를 알려준다. 당근의 크기가 수확한 순서로 주어질 때, 선별기가 알려준 연속으로 커지는 당근의 갯수는 최대 얼마인지 확인하기 위한 프로그램을 만드시오. 연속으로 커지지않는 경우 구간의 최소 길이는 1이다.
N개의 당근을 수확하며, 당근의 크기 C는 1부터 10까지의 정수로 정해진다.
5<=N<=1000, 1<=C<=10

입력
첫 줄에 테스트케이스의 개수 T, 다음 줄 부터 테스트케이스별로 첫 줄에 당근 개수 N, 다음 줄 당근의 크기 C를 의미하는 N개의 정수가 주어진다.

출력
#테스트케이스번호와 연속으로 커지는 당근 개수의 최대값을 출력한다.


'''

import sys
sys.stdin = open('input.txt', 'r')

def max_count(li):   # 맥스값 찾기
    count = 0
    for a in li:
        if count < a:
            count = a
    return count


T = int(input())  # 테스트 케이스 수

for case in range(1, T+1):
    N = int(input())  # 당근의 개수 N
    C = list(map(int, input().split()))   # 당근의 크기 C
    C.append(0)    # 값 끝까지 비교하기 위해 0 더해줌
    zero_arr = [0]*(N)  # 빈배열 생성

    count = 1  # 처음 시작 값 count 1로 할당
    for c in range(N):
        if C[c+1] > C[c]:  # 증가
            zero_arr[c] = count
            count+=1   # 값 증가

        else:
            zero_arr[c] = count
            count = 1
    print(f'#{case} {max_count(zero_arr)}')