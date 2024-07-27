'''
1933. 간단한 N의 약수

입력으로 1개의 정수 N 이 주어진다.
정수 N 의 약수를 오름차순으로 출력하는 프로그램을 작성하라.

[제약사항]
N은 1이상 1,000이하의 정수이다. (1 ≤ N ≤ 1,000)

[입력]
입력으로 정수 N 이 주어진다.

[출력]
정수 N 의 모든 약수를 오름차순으로 출력한다.
'''

num = int(input())
factors = []

# 나머지가 0인 수가 약수!!
for i in range(1, num+1): 
    if num % i == 0:
        factors.append(i)

# 혹시 모르니 오름차순으로 정렬
factors.sort()

# join 함수 int에 사용하려면 map() 사용하기!!
print(' '.join(map(str,factors)))