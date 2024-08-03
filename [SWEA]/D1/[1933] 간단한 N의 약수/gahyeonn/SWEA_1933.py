num = int(input())

lst = []
for i in range(1, num+1) :

    if num % i == 0 : # 약수이면
        lst.append(i) # lst에 append
        a = lst.pop() # append와 동시에 pop
        print(a, end = ' ') # pop한 값 출력

