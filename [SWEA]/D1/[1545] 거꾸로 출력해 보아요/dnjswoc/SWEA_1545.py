'''
주어진 숫자부터 0까지 순서대로 찍어보세요
아래는 입력된 숫자가 N일 때 거꾸로 출력하는 예시입니다.
N N-1 N-2 ... 0
'''

N = int(input())
reverse = []
for i in range(N+1):
    reverse.append(f'{str(N-i)} ')
print(''.join(reverse))
# reverse라는 빈 리스트를 만들어 입력 받은 숫자를 string 형식의 역순으로 리스트에 저장하고
# 마지막 code로 ''(따옴표)없이 리스트를 출력했습니다.