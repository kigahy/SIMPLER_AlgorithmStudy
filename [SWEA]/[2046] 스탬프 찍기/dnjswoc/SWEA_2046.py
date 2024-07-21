'''
주어진 숫자만큼 #을 출력해보세요.
주어질 숫자는 100,000 이하다.
'''

num = int(input())
# 출력할 #의 개수를 받는다.

list_of_sharp = []
for i in range(num):
    list_of_sharp.append('#')
# 빈 리스트를 만들어 입력받은 수만큼의 #을 리스트에 넣는다.

print(''.join(list_of_sharp))
# #이 들어간 리스트를 ''없이 붙어서 출력한다.