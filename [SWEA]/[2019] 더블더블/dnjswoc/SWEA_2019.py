'''
1부터 주어진 횟수까지 2를 곱한 값(들)을 출력하시오.
주어질 숫자는 30을 넘지 않는다.
'''

N = int(input())
multipled_number = []       # 2가 곱해져 출력될 수
number=1
for i in range(1, N+2):     # 입력될 수가 N+1개라서
    multipled_number.append(f'{number} ')
    number*=2
print(''.join(multipled_number))