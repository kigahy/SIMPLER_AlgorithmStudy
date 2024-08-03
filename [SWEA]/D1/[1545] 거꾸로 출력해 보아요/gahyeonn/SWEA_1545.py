import copy # 깊은 복사

num = int(input()) + 1
lst = [] # input값 저장
cop = [] # pop했을 때 lst 길이 줄지 않기 위한 복사 리스트

for i in range(num) :
    lst.append(i) # num으로 복사받은 값을 lst에 저장

cop = copy.deepcopy(lst) #cop에 lst 깊은복사

for j in lst :
    print(cop.pop(), end = ' ') # lst 크기만큼 pop, 값은 cop에서 pop